"""main application for FastAPI."""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import render, anime
from app import models
from app.database import engine

import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")
app.include_router(render.router)
app.include_router(anime.router, prefix="/api/v1")

if __name__ == '__main__':
  uvicorn.run(app, host='127.0.0.1', port=8000)