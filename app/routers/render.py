from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from .anime import read_trend

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse, include_in_schema=False)
def render_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "id": id})


@router.get("/popular-anime", response_class=HTMLResponse, include_in_schema=False)
def render_popular_anime(request: Request):
    return templates.TemplateResponse("popular.html", {"request": request, "id": id})


@router.get("/genres", response_class=HTMLResponse, include_in_schema=False)
def render_genres_count(request: Request):
    return templates.TemplateResponse(
        "catagories_count.html", {"request": request, "id": id}
    )
