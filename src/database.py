import psycopg2


class Database:
    connection = None

    @classmethod
    def setup(cls):
        # TODO: use environment variables
        cls.connection = psycopg2.connect('host=secret dbname=secret user=secret password=secret')
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
