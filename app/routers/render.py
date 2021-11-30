from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.routers.anime import read_trend

router = APIRouter(tags=["templates"])

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def render_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "id": id})


@router.get("/popular-anime", response_class=HTMLResponse)
async def render_popular_anime(request: Request):
    data = await read_trend()
    return templates.TemplateResponse(
        "popular.html", {"request": request, "id": id, "data": data}
    )


@router.get("/genres", response_class=HTMLResponse)
def render_genres_count(request: Request):
    return templates.TemplateResponse(
        "catagories_count.html", {"request": request, "id": id}
    )


@router.get("/age_rating", response_class=HTMLResponse)
def render_agerating(request: Request):
    return templates.TemplateResponse("age_rating.html", {"request": request, "id": id})

@router.get("/first_introduced", response_class=HTMLResponse)
def render_agerating(request: Request):
    return templates.TemplateResponse("first_introduced.html", {"request": request, "id": id})