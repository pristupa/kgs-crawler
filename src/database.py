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
            "id SERIAL PRIMARY KEY, "
            "nickname VARCHAR(10) UNIQUE"
            ")",
        )
        cursor.close()
        cls.connection.commit()

    @classmethod
    def teardown(cls):
        if cls.connection is not None:
            cls.connection.close()
