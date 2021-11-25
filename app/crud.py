from sqlalchemy.orm import Session

from . import models, schemas


def get_anime(db: Session, anime_id: int):
    return db.query(models.Anime).filter(models.Anime.id == user_id).first()


def get_anime_by_name(db: Session, title: str):
    return db.query(models.Anime).filter(models.Anime.email == title).first()


def create_anime(db: Session, anime: schemas.Anime):
    db_anime = models.Anime(title=anime.title, body=anime.body)
    db.add(db_anime)
    db.commit()
    db.refresh(db_anime)
    return db_anime


def get_anime_list(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Anime).offset(skip).limit(limit).all()


def update_anime(db: Session, anime_id: int, data: schemas.Anime):
    db_anime = db.query(models.Anime).filter(models.Anime.id == anime_id)
    if db_anime:
        db_anime.update(data)
        db.commit()
        return True
    return False

def destroy_anime(db: Session, anime_id: int):
    db_anime = db.query(models.Anime).filter(models.Anime.id == anime_id)
    if db_anime: 
        db_anime.delete(synchronize_session=False)
        db.commit()
        return True