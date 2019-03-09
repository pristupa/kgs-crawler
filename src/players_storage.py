from .cache import Cache
from .database import Database


class PlayersStorage:

    @classmethod
    def add_player(cls, nickname: str) -> bool:
        if Cache.has_player(nickname):
            return False

        cursor = Database.connection.cursor()
        cursor.execute("INSERT INTO players (nickname) VALUES (%s) ON CONFLICT (nickname) DO NOTHING", (nickname,))
        rowcount = cursor.rowcount
        cursor.close()
        Cache.add_player(nickname)
        return rowcount > 0
