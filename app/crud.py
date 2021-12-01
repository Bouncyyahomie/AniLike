"""Crud method of the database."""
from sqlalchemy.orm import Session
from typing import Dict
from .database import db_cursor
from . import schemas
import csv


async def read_anime(anime_id: int):
    with db_cursor() as cs:
        cs.execute(
            """
            SELECT *
            FROM AnilikeResponse
            WHERE id = %s
        """,
            [anime_id],
        )
    result = cs.fetchone()
    if result:
        return result


async def read_all_anime():
    with db_cursor() as cs:
        cs.execute(
            """
            SELECT *
            FROM AnilikeResponse
        """
        )
        result = cs.fetchall()
        if len(result) >= 1:
            return result


async def create_anime(anime):
    with db_cursor() as cs:
        cs.execute(
            """ 
            INSERT INTO
        """,
            [anime],
        )


async def update_anime(record_id, data):
    with db_cursor() as cs:
        cs.execute(
            """ 
            UPDATE AnimeQuestionnaire 
            SET 
            WHERE id = %s
        """,
            [data, record_id],
        )


async def delete_anime(record_id):
    with db_cursor() as cs:
        cs.execute(
            """ 
            DELETE FROM AnimeQuestionnaire
            WHERE id = %s
        """,
            [record_id],
        )
