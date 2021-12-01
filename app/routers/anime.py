"""API router for anime."""
from fastapi import APIRouter, Depends, status, HTTPException
from starlette.status import HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT
from app import fetch_api
from app import schemas

from typing import List
from .. import crud


router = APIRouter(tags=["complex"])


@router.get("/demo", include_in_schema=False)
async def read_anime():
    data = []
    url = "https://kitsu.io/api/edge"
    name_list = ["inuyasha", "one piece", "naruto", "bleach", "gintama"]
    for name in name_list:
        data.append(fetch_api.kitsu_get_rating(url=url, name=name))
    return {"messages": data}


@router.get("/anilist")
async def read_ani():
    data = fetch_api.anilist_read()
    return data


@router.get("/trend")
async def read_trend():
    return fetch_api.kitsu_get_trend_anime()


@router.get("/genres")
async def get_genres():
    data = fetch_api.kitsu_get_catagories()
    return data


@router.get("/agerating")
async def get_agerating():
    data = fetch_api.kitsu_get_age_rating()
    return data


@router.get("/first_introduced")
async def get_introducedBy():
    data = fetch_api.get_introduced()
    return data


@router.get("/mysql/")
async def retrive():
    anime = crud.init_data_base()
    return anime


@router.get("/season_trend/{season}/{year}")
async def jikan_get_season(season: str, year):
    anime = fetch_api.jikan_get_season_and_year(season, year)
    return anime
