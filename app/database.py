"""Database configuration."""
from .config import DB_HOST, DB_USER, DB_PASSWD, DB_NAME
import pymysql as mysql


def db_cursor():
    return mysql.connect(
        host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, db=DB_NAME
    ).cursor()
