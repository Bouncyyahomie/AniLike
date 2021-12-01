"""API router for anime."""
from fastapi import APIRouter, HTTPException, status
from starlette.status import HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT
from app import schemas

from .. import crud


router = APIRouter(tags=["basic routes"])


@router.get("/")
async def get_anime():
    """
    # Retrive anime list
    """
    anime_list = await crud.read_all_anime()
    return anime_list


@router.get("/{id}", response_model=schemas.ShowAnime)
async def show_anime(id):
    """
    # Retrive a anime
    - **id** : a valid data id in database.
    """
    anime = await crud.read_anime(anime_id=id)
    if not anime:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": f"Anime id {id} not found"},
        )
    return anime


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Anime):
    """
    # Create a new questionnaire record
    - **title** = str
    - **age** = int
    - **gender** = str
    - **genre** = str
    - **watch_frequency** = str
    - **introduced_by** = str
    - **favorite** = str
    - **sub_dub** = str
    - **how_long** = str
    - **interest_in** = str
    """
    return await crud.create_anime(anime=request)


@router.delete("/{id}", status_code=HTTP_204_NO_CONTENT)
async def destroy(id):
    """
    # Create a new anime
    - **id** : deleted record id.
    """
    if not await crud.delete_anime(record_id=id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": f"Anime id {id} not found"},
        )
    return {"message": f"anime id {id} remove success"}


@router.put("/{id}", status_code=HTTP_202_ACCEPTED)
async def update(id, request: schemas.Anime):
    """
    # Create a new anime
    - **id** : updated anime id.
    """
    if not await crud.update_anime(record_id=id, anime=request):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": f"Anime id {id} not found"},
        )
    return {"message": f"anime id {id} updated success"}
