"""Crud method of the database."""
from sqlalchemy.orm import Session
from typing import Dict
from .database import db_cursor
from . import schemas
import csv


def extract_csv():
    data = []
    with open("DAQ project (Responses) - Form Responses 1.csv") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",")
        for row in spamreader:
            data.append(row)
    return data


async def read_anime(anime_id: int):
    with db_cursor() as cs:
        cs.execute(
            """
            SELECT *
            FROM AnimeQuestionnaire
            WHERE id = %s
        """[
                anime_id
            ]
        )
    result = cs.fetchone()
    if result:
        return result


async def read_all_anime():
    with db_cursor() as cs:
        cs.execute(
            """
            SELECT *
            FROM AnimeQuestionnaire
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
        """
        )


async def update_anime(record_id, data):
    with db_cursor() as cs:
        cs.execute(
            """ 
            UPDATE AnimeQuestionnaire 
            SET 
            WHERE id = %s
        """,
            [record_id],
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


def init_data_base():
    with db_cursor() as cs:
        cs.execute(
            """ 
            SELECT *
            FROM AnimeQuestionnaire
        """
        )
        result = cs.fetchall()
        if len(result) > 1:
            return result

        # cs.execute("""
        #     INSERT INTO AnimeQuestionnaire(id, title, age, gender, favorite genre, watch frequency, introduced by, favorite anime, sub or dub, interest in, timestamp)
        #     VALUES ()
        # """)
        # result = cs.fetchall()
        result = extract_csv()

        return result
