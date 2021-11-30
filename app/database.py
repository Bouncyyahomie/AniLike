"""Database configuration."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv
# from . import crud

SQLALCHEMY_DATABASE_URL = "sqlite:///./anime.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        print("error")
    finally:
        db.close()

# from .config import DB_HOST, DB_USER, DB_PASSWD, DB_NAME
# import pymysql as mysql

# def db_cursor():
#     return mysql.connect(host=DB_HOST,
#                          user=DB_USER,
#                          passwd=DB_PASSWD,
#                          db=DB_NAME).cursor()

