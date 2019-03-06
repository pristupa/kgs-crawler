import urllib.request


class KGSClient:
    BASE_URL = 'https://www.gokgs.com'

    def download_month_archive(self, nickname: str, year: int, month: int) -> bytes:
        url = f'{self.BASE_URL}/servlet/archives/ru_RU/{nickname}-{year}-{month}.zip'
        with urllib.request.urlopen(url) as zip_file:
            return zip_file.read()
