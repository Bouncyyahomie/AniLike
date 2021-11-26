import requests
from operator import itemgetter

kitsu_base_url = "https://kitsu.io/api/edge"
mal_base_url = "https://api.myanimelist.net/v2"
anilist_base_url = "https://graphql.anilist.co"


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
            d = {"title": attr["title"],
                "total_media_count": attr["totalMediaCount"]}
            data_list.append(d)
        curr_url = next_url
    print("end")
    data_list.sort(key=itemgetter("title"))
    return data_list


def kitsu_get_trend_anime():
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
    return data_list


def kitsu_get_age_rating():
    print("start")
    data_list = []
    curr_url = (
        f"https://kitsu.io/api/edge/anime?page%5Blimit%5D=20&page%5Boffset%5D=0"
    )
    next_url = ""
    last_url = (
        "https://kitsu.io/api/edge/anime?page%5Blimit%5D=20&page%5Boffset%5D=17000"
    )
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
            d = {"Title": attr["canonicalTitle"],
                 "ageRating": attr["ageRating"],
                "ageRatingGuide": attr["ageRatingGuide"]}
            data_list.append(d)
        curr_url = next_url
    print("end")
    data_list.sort(key=itemgetter("ageRatingGuide"))
    return data_list



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
