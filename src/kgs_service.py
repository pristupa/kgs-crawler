import re
from html.parser import HTMLParser
from io import BytesIO
from zipfile import ZipFile

from .archives_storage import ArchivesStorage
from .database import Database
from .kgs_client import KGSClient
from .sgf import Game
from .sgf import Color
from .players_storage import PlayersStorage
from .games_storage import GamesStorage

link_regexp = re.compile('gameArchives\.jsp\?user=([^&]+)&year=(\d+)&month=(\d+)')


class _ArchivesPageParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        attrs = dict(attrs)
        href = attrs.get('href', '')
        match = link_regexp.match(href)
        if match is not None:
            nickname, year, month = match.groups()
            year = int(year)
            month = int(month)
            ArchivesStorage.add_month_record(nickname, year, month)


class KGSService:

    def __init__(self):
        self._client = KGSClient()
        self._archives_page_parser = _ArchivesPageParser()

    def try_load_games_for_month(self):
        cursor = Database.connection.cursor()
        cursor.execute(
            "SELECT nickname, archive_month FROM archives WHERE downloaded=FALSE ORDER BY archive_month LIMIT 1"
        )
        nickname, archive_month = cursor.fetchone()
        cursor.close()
        year, month = archive_month.split('-')
        year = int(year)
        month = int(month)
        self.load_games_for_month(nickname, year, month)

    def load_games_for_month(self, nickname: str, year: int, month: int, manual: bool = False):
        if manual:
            ArchivesStorage.add_month_record(nickname, year, month)
        print(f'Loading games archive for {month:02}/{year} for {nickname}...')
        archive_month = f'{year}-{month}'

        cursor = Database.connection.cursor()
        cursor.execute(
            "SELECT 1 FROM archives WHERE nickname=%s AND archive_month=%s FOR UPDATE",
            (nickname, archive_month),
        )
        zip_data = self._client.download_month_archive(nickname, year, month)
        zip_file = ZipFile(file=BytesIO(zip_data))
        for sgf_file_name in zip_file.namelist():
            sgf_file = zip_file.open(sgf_file_name)
            try:
                sgf_content = sgf_file.read()
            finally:
                sgf_file.close()
            game = Game(sgf_content)

            black_nickname = game.get_player_nickname(Color.BLACK)
            if PlayersStorage.add_player(black_nickname):
                self.load_months_for_player(black_nickname)

            white_nickname = game.get_player_nickname(Color.WHITE)
            if PlayersStorage.add_player(white_nickname):
                self.load_months_for_player(white_nickname)

            GamesStorage.add_game(game, raw_sgf_content=sgf_content)
        cursor.execute(
            "UPDATE archives SET downloaded=TRUE WHERE nickname=%s AND archive_month=%s",
            (nickname, archive_month),
        )
        cursor.close()
        Database.connection.commit()

    def load_months_for_player(self, nickname: str):
        archives_page = self._client.get_archives_page(nickname)
        self._archives_page_parser.feed(archives_page)
