from typing import List
from typing import Tuple

import psycopg2

from .settings import settings


class Database:
    connection = None

    @classmethod
    def setup(cls):
        connection_string = 'host={host} dbname={name} user={user} password={password}'.format(
            host=settings.db_host,
            name=settings.db_name,
            user=settings.db_user,
            password=settings.db_password,
        )
        cls.connection = psycopg2.connect(connection_string)
        cls.execute(
            "CREATE TABLE IF NOT EXISTS players ("
            "id SERIAL PRIMARY KEY,"
            "nickname VARCHAR(20) UNIQUE NOT NULL"
            ")",
        )
        cls.execute(
            "CREATE TABLE IF NOT EXISTS archives ("
            "id SERIAL PRIMARY KEY,"
            "nickname VARCHAR(10) NOT NULL,"
            "archive_month VARCHAR(7) NOT NULL,"
            "downloaded BOOLEAN DEFAULT NULL,"
            "UNIQUE (nickname, archive_month)"
            ")"
        )
        cls.execute(
            "CREATE TABLE IF NOT EXISTS games ("
            "id SERIAL PRIMARY KEY,"
            "year SMALLINT NOT NULL,"
            "month SMALLINT NOT NULL,"
            "played_at DATE,"
            "white_nickname VARCHAR(20) NOT NULL,"
            "black_nickname VARCHAR(20) NOT NULL,"
            "white_rank TEXT,"
            "black_rank TEXT,"
            "white_won BOOLEAN,"
            "board_size SMALLINT NOT NULL,"
            "komi REAL NOT NULL,"
            "handicap SMALLINT NOT NULL,"
            "timelimit REAL,"
            "overtime TEXT,"
            "sgf_content BYTEA NOT NULL,"
            "sgf_content_hash CHAR(40) UNIQUE NOT NULL"
            ")"
        )
        cls.connection.commit()

    @classmethod
    def teardown(cls):
        if cls.connection is not None:
            cls.connection.close()

    @classmethod
    def fetch_all(cls, *args) -> List[Tuple]:
        cursor = cls.connection.cursor()
        cursor.execute(*args)
        result = cursor.fetchall()
        cursor.close()
        return result

    @classmethod
    def fetch_one(cls, *args) -> Tuple:
        cursor = cls.connection.cursor()
        cursor.execute(*args)
        result = cursor.fetchone()
        cursor.close()
        return result

    @classmethod
    def execute(cls, *args) -> int:
        cursor = cls.connection.cursor()
        cursor.execute(*args)
        rowcount = cursor.rowcount
        cursor.close()
        return rowcount
