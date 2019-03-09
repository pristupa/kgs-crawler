from .cache import Cache
from .database import Database


class PlayersStorage:

    @classmethod
    def add_player(cls, nickname: str) -> bool:
        if Cache.has_player(nickname):
            return False

        rowcount = Database.execute(
            "INSERT INTO players (nickname) VALUES (%s) ON CONFLICT (nickname) DO NOTHING",
            (nickname,),
        )
        Cache.add_player(nickname)
        return rowcount > 0
