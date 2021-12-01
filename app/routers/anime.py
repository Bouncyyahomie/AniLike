"""API router for anime."""
from typing import List
from fastapi import APIRouter
from app import fetch_api
from .. import crud, schemas


router = APIRouter(tags=["complex"])


@router.get("/popular-anime", response_model=List[schemas.ShowTrendAnime])
async def read_trend():
    """
    # Return a top 10 popular anime list with their average rating.
    """
    return fetch_api.kitsu_get_trend_anime()


@router.get("/genres", response_model=List[schemas.ShowGenre])
async def get_genres():
    """
    # Return a list of genres with total anime count.
    """
    data = fetch_api.kitsu_get_catagories()
    return data


@router.get("/agerating")
async def get_agerating():
    """
    # Return a age rating list with total anime with that rating.
    """
    data = fetch_api.kitsu_get_age_rating()
    return data


@router.get("/first_introduced", response_model=List[List[schemas.ShowIntroduce]])
async def get_introducedBy():
    """
    # Return methods list that people introduced to anime with their count.
    """
    data = fetch_api.get_introduced()
    return data


@router.get("/season_trend/{season}/{year}")
async def jikan_get_season(season: str, year):
    """ 
    # Return a top 5 anime list by given airing season and year.
    - **season** : a valid season ("winter", "spring", "summer", "fall")
    - **year**: a valid year.
    """
    anime = fetch_api.jikan_get_season_and_year(season, year)
    return anime
