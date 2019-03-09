import urllib.request


class KGSClient:
    BASE_URL = 'https://www.gokgs.com/'

    def download_month_archive(self, nickname: str, year: int, month: int) -> bytes:
        url = self.BASE_URL + f'servlet/archives/ru_RU/{nickname}-{year}-{month}.zip'
        print(f'Downloading {url}')
        # TODO: Handle 404
        with urllib.request.urlopen(url) as zip_file:
            return zip_file.read()

    def get_archives_page(self, nickname: str) -> bytes:
        url = self.BASE_URL + f'gameArchives.jsp?user={nickname}'
        print(f'Downloading {url}')
        with urllib.request.urlopen(url) as archives_page:
            return archives_page.read()
