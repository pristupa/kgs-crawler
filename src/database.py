import sqlite3
from sqlite3 import Connection


class Database:
    connection: Connection = None

    @classmethod
    def setup(cls):
        cls.connection = sqlite3.connect('kgs.db')
        cursor = cls.connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS players ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "nickname VARCHAR(10) UNIQUE"
            ")",
        )
        cls.connection.commit()

    @classmethod
    def teardown(cls):
        if cls.connection is not None:
            cls.connection.close()
