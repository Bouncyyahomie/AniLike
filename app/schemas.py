"""pydantic model."""
from pydantic import BaseModel


class Anime(BaseModel):
    title: str
    body: str


class ShowAnime(Anime):
    class Config:
        orm_mode = True
