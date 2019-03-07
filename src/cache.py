from .database import Database


class Cache:
    nicknames = set()

    @classmethod
    def warmup(cls):
        cursor = Database.connection.cursor()
        cursor.execute("SELECT nickname FROM players")
        for nickname, in cursor.fetchall():
            cls.nicknames.add(nickname)
        cursor.close()

    @classmethod
    def has_player(cls, nickname: str):
        return nickname in cls.nicknames

    @classmethod
    def add_player(cls, nickname: str):
        cls.nicknames.add(nickname)
