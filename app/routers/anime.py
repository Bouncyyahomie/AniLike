from fastapi import APIRouter
from app.fetch_api import get_rating

router = APIRouter()


@router.get("/")
async def read_anime():
    data = []
    url = "https://kitsu.io/api/edge"
    name_list = ["inuyasha", "one piece", "naruto", "bleach", "gintama"]
    for name in name_list:
        data.append(get_rating(url=url, name=name))
    return {"messages": data}

@router.get("/top")
async def read_top_anime():
    pass

@router.get("/{genre_id}")
async def read_genre():
    pass


