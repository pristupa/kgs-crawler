from .cache import Cache
from .database import Database


class PlayersStorage:

    @classmethod
    def add_player(cls, nickname: str):
        if Cache.has_player(nickname):
            return

        Cache.add_player(nickname)
        cursor = Database.connection.cursor()
        cursor.execute("INSERT INTO players (nickname) VALUES (%s) ON CONFLICT (nickname) DO NOTHING", (nickname,))
        cursor.close()
        Database.connection.commit()
