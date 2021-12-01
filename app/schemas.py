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


class ShowTrendAnime(BaseModel):
    title: str
    average_rating: str
    popularity_rank: int


class ShowGenre(BaseModel):
    title: str
    total_media_count: int


class ShowIntroduce(BaseModel):
    first_introduced_by: str
    count: int


class ShowRating(BaseModel):
    title: str
    rating: int
