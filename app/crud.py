"""Crud method of the database."""
from .database import db_cursor


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
            INSERT INTO `AnimeQuestionnaire(age, gender, `favorite genre`, `watch frequency`, `introduced by`, `favorite anime`, `sub or dub`, `how long`, `interest in`) 
            VALUES (%s, %s,%s,%s, %s,%s,%s, %s,%s)
        """,
            [anime.age, anime.gender, anime.watch_frequency, anime.introduced_by, anime.favorite, anime.sub_dub, anime.how_long, anime.interest_in],
        )


async def update_anime(record_id, anime):
    with db_cursor() as cs:
        cs.execute(
            """ 
            UPDATE `AnimeQuestionnaire`
            SET age=%s, gender=%s, `favorite genre`=%s, `watch frequency`=%s, `introduced by`=%s, `favorite anime`=%s, `sub or dub`=%s, `how long`=%s, `interest in`=%s
            WHERE id = %s
        """,
            [anime.age, anime.gender, anime.watch_frequency, anime.introduced_by, anime.favorite, anime.sub_dub, anime.how_long, anime.interest_in, record_id],
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


async def get_introduced():
    with db_cursor() as cs:
        cs.execute("SELECT `introduced by` FROM AnilikeResponse")
    return [row[0] for row in cs.fetchall()]
