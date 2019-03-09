from .database import Database


class Cache:
    archives = {}
    games = set()

    @classmethod
    def warmup(cls):
        cursor = Database.connection.cursor()
        cursor.execute("SELECT nickname, archive_month FROM archives")
        for nickname, archive_month in cursor.fetchall():
            cls.add_player(nickname)
            year, month = archive_month.split('-')
            cls.add_month(nickname, int(year), int(month))
        cursor.close()

    @classmethod
    def has_player(cls, nickname: str):
        return nickname in cls.archives

    @classmethod
    def add_player(cls, nickname: str):
        if nickname not in cls.archives:
            cls.archives[nickname] = set()

    @classmethod
    def has_month(cls, nickname: str, year: int, month: int) -> bool:
        return (year, month) in cls.archives[nickname]

    @classmethod
    def add_month(cls, nickname: str, year: int, month: int):
        cls.archives[nickname].add((year, month))

    @classmethod
    def has_game(cls, sgf_content_hash: str) -> bool:
        return sgf_content_hash in cls.games

    @classmethod
    def add_game(cls, sgf_content_hash: str):
        cls.games.add(sgf_content_hash)
