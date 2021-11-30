"""pydantic model."""
from pydantic import BaseModel


class Anime(BaseModel):
    title = str
    age = int
    gender = str
    genre = str
    watch_frequency = str
    introduced_by = str
    favorite = str
    sub_dub = str
    interest_in = str


class ShowAnime(Anime):
    class Config:
        orm_mode = True
