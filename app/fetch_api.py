import requests
from operator import itemgetter
import pymysql.cursors
from app.config import DB_HOST,DB_USER,DB_PASSWD,DB_NAME,DB_TABLE

kitsu_base_url = "https://kitsu.io/api/edge"
mal_base_url = "https://api.myanimelist.net/v2"
anilist_base_url = "https://graphql.anilist.co"

mydb = pymysql.connect(
    host=DB_HOST,
    user=DB_USER, 
    password=DB_PASSWD,
    database=DB_NAME,
    cursorclass=pymysql.cursors.DictCursor
)
mycursor = mydb.cursor()

def get_introduced():
    data = []
    friend, tele, vg, internet = 0, 0, 0, 0
    mycursor.execute(f"SELECT `introduced by` FROM {DB_TABLE}")
    myresult = mycursor.fetchall()
    for x in myresult:
        if x["introduced by"] == 'By a friend':
            friend+=1
        if x["introduced by"] == 'Television':
            tele+=1
        if x["introduced by"] == 'Video Game':
            vg+=1
        if x["introduced by"] == 'The Internet':
            internet+=1
    fr = {"first_introduced_by": 'By a friend', "count": friend},{"first_introduced_by": "Television", "count": tele},{"first_introduced_by": "Video Game", "count":vg},{"first_introduced_by": "Internet", "count": internet}
    data.append(fr)
    return data
    

def kitsu_get_rating(url, name: str):
    q = {"filter[text]": name}
    res = requests.get(url=f"{url}/anime", params=q)
    content = res.json()["data"][0]
    data = {
        "title": content["attributes"]["titles"]["en"],
        "rating": content["attributes"]["averageRating"],
    }
    return data


def kitsu_get_catagories():
    print("start")
    data_list = []
    curr_url = (
        f"https://kitsu.io/api/edge/categories?page%5Blimit%5D=10&page%5Boffset%5D=0"
    )
    next_url = ""
    last_url = (
        "https://kitsu.io/api/edge/categories?page%5Blimit%5D=10&page%5Boffset%5D=210"
    )
    while curr_url != last_url:
        res = requests.get(url=curr_url)
        content = res.json()
        next_url = content["links"]["next"]
        data = content["data"]
        for anime in data:
            attr = anime["attributes"]
            d = {"title": attr["title"], "total_media_count": attr["totalMediaCount"]}
            data_list.append(d)
        curr_url = next_url
    print("end")
    data_list.sort(key=itemgetter("title"))
    return data_list


def kitsu_get_trend_anime():
    print("start")
    url = "https://kitsu.io/api/edge/trending/anime"
    res = requests.get(url=url)
    content = res.json()["data"]
    data_list = []
    for anime in content:
        data = {
            "title": anime["attributes"]["titles"]["en_jp"],
            "averageRating": anime["attributes"]["averageRating"],
            "popularityRank": anime["attributes"]["popularityRank"],
        }
        data_list.append(data)
    data_list.sort(key=itemgetter("popularityRank"))
    print("end")
    return data_list


def kitsu_get_age_rating():
    print("start")
    data_count = []
    curr_url = f"https://kitsu.io/api/edge/anime?page%5Blimit%5D=20&page%5Boffset%5D=0"
    next_url = ""
    last_url = (
        "https://kitsu.io/api/edge/anime?page%5Blimit%5D=20&page%5Boffset%5D=17000"
    )
    vp17, aa, cd, md, ndt, too, vp = 0, 0, 0, 0, 0, 0, 0
    while curr_url != last_url:
        res = requests.get(url=curr_url)
        content = res.json()
        print(curr_url)
        next_url = content["links"]["next"]
        data = content["data"]
        for anime in data:
            attr = anime["attributes"]
            if not attr["ageRatingGuide"]:
                continue
            if attr["ageRatingGuide"] == "17+ (violence & profanity)":
                vp17 += 1
            if attr["ageRatingGuide"] == "All Ages":
                aa += 1
            if attr["ageRatingGuide"] == "Children":
                cd += 1
            if attr["ageRatingGuide"] == "Mild Nudity":
                md += 1
            if attr["ageRatingGuide"] == "Nudity":
                ndt += 1
            if attr["ageRatingGuide"] == "Teens 13 or older":
                too += 1
            if attr["ageRatingGuide"] == "Violence, Profanity":
                vp += 1
        curr_url = next_url
    vp17d = {"title": "17+ (violence & profanity)", "mediaCount": vp17}
    aad = {"title": "All Ages", "mediaCount": aa}
    cdd = {"title": "Children", "mediaCount": cd}
    mdd = {"title": "Mild Nudity", "mediaCount": md}
    ndtd = {"title": "Nudity", "mediaCount": ndt}
    tood = {"title": "Teens 13 or older", "mediaCount": too}
    vpd = {"title": "Violence, Profanity", "mediaCount": vp}
    data_count.append(vp17d)
    data_count.append(aad)
    data_count.append(cdd)
    data_count.append(mdd)
    data_count.append(ndtd)
    data_count.append(tood)
    data_count.append(vpd)
    print("end")
    return data_count


def anilist_read():

    # Here we define our query as a multi-line string
    query = """
    query ($id: Int) { # Define which variables will be used in the query (id)
        Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
        id
        title {
        romaji
        english
        native
        }
    }
    }
    """

    # Define our query variables and values that will be used in the query request
    variables = {"id": 15125}

    url = "https://graphql.anilist.co"

    # Make the HTTP Api request
    response = requests.post(url, json={"query": query, "variables": variables})
    print(response.text)
