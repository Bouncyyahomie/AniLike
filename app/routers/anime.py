"""API router for anime."""
from fastapi import APIRouter, Depends, status, HTTPException
from starlette.status import HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT
from app.fetch_api import get_rating
from app import schemas
from app.database import get_db
from sqlalchemy.orm import Session
from typing import List
from .. import crud


router = APIRouter()


@router.get("/demo", include_in_schema=False)
async def read_anime():
    data = []
    url = "https://kitsu.io/api/edge"
    name_list = ["inuyasha", "one piece", "naruto", "bleach", "gintama"]
    for name in name_list:
        data.append(get_rating(url=url, name=name))
    return {"messages": data}


@router.get("/top", include_in_schema=False)
async def read_top_anime():
    pass


@router.get("/{genre_id}", include_in_schema=False)
async def read_genre():
    pass


@router.get("/", response_model=List[schemas.ShowAnime])
async def get_anime(db: Session = Depends(get_db)):
    """
    # Retrive anime list
    """
    anime_list = crud.get_anime_list(db=db)
    return anime_list


@router.get("/{id}", response_model=schemas.ShowAnime)
async def show_anime(id, db: Session = Depends(get_db)):
    """
    # Retrive a anime
    """
    anime = crud.get_anime(db=db, anime_id=id)
    if not anime:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": f"Anime id {id} not found"},
        )
    return anime


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Anime, db: Session = Depends(get_db)):
    """
    # Create a new anime
    - **title** : a new anime title.
    """
    return crud.create_anime(db=db, anime=request)


@router.delete("/{id}", status_code=HTTP_204_NO_CONTENT)
async def destroy(id, db: Session = Depends(get_db)):
    """
    # Create a new anime
    - **id** : deleted anime id.
    """
    if not crud.destroy_anime(db=db, anime_id=id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": f"Anime id {id} not found"},
        )
    return {"message": f"anime id {id} remove success"}


@router.put("/{id}", status_code=HTTP_202_ACCEPTED)
async def update(id, request: schemas.Anime, db: Session = Depends(get_db)):
    """
    # Create a new anime
    - **id** : updated anime id.
    """
    if not crud.update_anime(db=db, anime_id=id, data=request):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": f"Anime id {id} not found"},
        )
    return {"message": f"anime id {id} updated success"}
