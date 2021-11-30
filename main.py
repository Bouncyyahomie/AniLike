"""main application for FastAPI."""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import basic, render, anime
from fastapi.middleware.cors import CORSMiddleware

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
    },
    {"name": "templates", "description": "template render route"},
]
version = "1"

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5050",
    "*",
]


app = FastAPI(
    title="Anilike",
    description=description,
    version=version,
    contact={
        "name": "",
    },
    openapi_tags=tags_metadata,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

app.include_router(render.router)
app.include_router(anime.router, prefix=f"/api/v{version}")
app.include_router(basic.router, prefix=f"/api/v{version}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5050, reload=True)
