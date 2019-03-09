from .cache import Cache
from .database import Database


class ArchivesStorage:

    @classmethod
    def add_month_record(cls, nickname: str, year: int, month: int):
        if Cache.has_month(nickname, year, month):
            return

        Database.execute(
            "INSERT INTO archives (nickname, archive_month) VALUES (%s, %s) "
            "ON CONFLICT (nickname, archive_month) DO NOTHING",
            (nickname, f'{year}-{month:02}'),
        )
        Cache.add_month(nickname, year, month)
