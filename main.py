"""main application for FastAPI."""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import basic, render, anime
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

description = """ 
Primary: [Questionnaire](https://docs.google.com/forms/d/e/1FAIpQLSfBJs1JBGDZqJdnWimzM7tng_TN4TQg2HygKHkxUzHc88GEzg/viewform)    
Secondary: API
- [Kitsu](https://kitsu.docs.apiary.io/)   
- [Jikan API Documentation (theapiguy) | RapidAPI](https://rapidapi.com/theapiguy/api/jikan1/)   
API Provide: Anime names, episodes, songs , start and end dates, etc.   
We aim to pair anime from input genre or find the best anime that is for you.   
Motivation: We aim to pair anime from input genre or find the best anime that is for you.
Pain points: Fetching data took too long because there’s too much data to process

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


app.include_router(render.router)
app.include_router(anime.router, prefix=f"/api/v{version}")
app.include_router(basic.router, prefix=f"/api/v{version}")
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5050, reload=True)
