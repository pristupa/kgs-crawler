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
        cursor = cls.connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS players ("
            "id SERIAL PRIMARY KEY,"
            "nickname VARCHAR(10) UNIQUE NOT NULL"
            ")",
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS archives ("
            "id SERIAL PRIMARY KEY,"
            "nickname VARCHAR(10) NOT NULL,"
            "archive_month VARCHAR(7) NOT NULL,"
            "downloaded BOOLEAN NOT NULL DEFAULT FALSE,"
            "UNIQUE (nickname, archive_month)"
            ")"
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS games ("
            "id SERIAL PRIMARY KEY,"
            "played_at DATE NOT NULL,"
            "white_nickname VARCHAR(10) NOT NULL,"
            "black_nickname VARCHAR(10) NOT NULL,"
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
        cursor.close()
        cls.connection.commit()

    @classmethod
    def teardown(cls):
        if cls.connection is not None:
            cls.connection.close()
