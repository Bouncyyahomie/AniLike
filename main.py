"""main application for FastAPI."""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import basic, render, anime
from app import models

import uvicorn

description = """ 

"""
tags_metadata = [
    {
        "name": "basic routes",
        "description": "basic crud operation",
    },
    {
        "name": "complex",
        "description": "",

    },{
        "name": "templates",
        "description": "template render route"
    }
]
version = "1"

app = FastAPI(
    title="Anilike",
    description=description,
    version=version,
    contact={
        "name": "",
    },
    openapi_tags=tags_metadata
)

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

app.include_router(render.router)
app.include_router(anime.router, prefix=f"/api/v{version}")
app.include_router(basic.router, prefix=f"/api/v{version}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5050, reload=True)
