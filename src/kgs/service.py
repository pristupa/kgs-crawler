from io import BytesIO
from zipfile import ZipFile

from .client import KGSClient
from .collector import KGSCollector
from .sgf import Game


class KGSService:

    def __init__(self):
        self._client = KGSClient()
        self._collector = KGSCollector()

    def load_games_for_month(self, nickname: str, year: int, month: int):
        zip_data = self._client.download_month_archive(nickname, year, month)
        zip_file = ZipFile(file=BytesIO(zip_data))
        for sgf_file_name in zip_file.namelist():
            sgf_file = zip_file.open(sgf_file_name)
            try:
                sgf_content = sgf_file.read()
            finally:
                sgf_file.close()
            game = Game(sgf_content)
            self._collector.store_game(game)
