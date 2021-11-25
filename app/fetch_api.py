import requests

kitsu_base_url = "https://kitsu.io/api/edge"
mal_base_url = "https://api.myanimelist.net/v2"
anilist_base_url = "https://graphql.anilist.co"



def get_rating(url, name: str):
    q = {"filter[text]": name}
    res = requests.get(url=f"{url}/anime", params=q)
    content = res.json()["data"][0]
    data = {
        "title": content["attributes"]["titles"]["en"],
        "rating": content["attributes"]["averageRating"]
    }
    return data
