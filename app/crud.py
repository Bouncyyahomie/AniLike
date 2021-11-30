"""Crud method of the database."""
from sqlalchemy.orm import Session
# from .database import get_db
from . import models, schemas
import csv

def get_anime(db: Session, anime_id: int):
    """Retrive anime that matching given id."""
    return db.query(models.QuestionnaireData).filter(models.QuestionnaireData.id == anime_id).first()


def get_anime_by_name(db: Session, title: str):
    """Retrive anime that matching given title."""
    return db.query(models.QuestionnaireData).filter(models.QuestionnaireData.email == title).first()


def create_anime(db: Session, anime: schemas.Anime):
    """Add a new anime to the database."""
    db_anime = models.QuestionnaireData(title=anime.title, age=anime.age, gender=anime.gender, genre=anime.genre, watch_frequency=anime.watch_frequency,
                                        introduced_by=anime.watch_frequency, favorite=anime.favorite, sub_dub=anime.sub_dub, interested_in=anime.interest_in)
    db.add(db_anime)
    db.commit()
    db.refresh(db_anime)
    return db_anime


def get_anime_list(db: Session, skip: int = 0, limit: int = 100):
    """Retrive anime list."""
    return db.query(models.QuestionnaireData).offset(skip).limit(limit).all()


def update_anime(db: Session, record_id: int, data: schemas.Anime):
    """Update a anime with a matching ID."""
    db_anime = db.query(models.QuestionnaireData).filter(
        models.QuestionnaireData.id == record_id)
    if db_anime:
        db_anime.update(data)
        db.commit()
        return True
    return False


def destroy_anime(db: Session, record_id: int):
    """Delete a anime with a matching ID."""
    db_anime = db.query(models.QuestionnaireData).filter(
        models.QuestionnaireData.id == record_id)
    if db_anime:
        db_anime.delete(synchronize_session=False)
        db.commit()
        return True


def init_data_base(db:Session):
    anime_id = 1
    first = db.query(models.QuestionnaireData).filter(models.QuestionnaireData.id == anime_id).first()
    if first:
        return