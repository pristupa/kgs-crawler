import requests
from fake_useragent import UserAgent


class KGSClient:
    BASE_URL = 'https://www.gokgs.com/'
    headers = {'User-Agent': str(UserAgent().chrome)}

    def download_month_archive(self, nickname: str, year: int, month: int) -> bytes:
        url = self.BASE_URL + f'servlet/archives/ru_RU/{nickname}-{year}-{month}.zip'
        print(f'Downloading {url}')
        # TODO: Handle 404
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise Exception(response.text)
        return response.content

    def get_archives_page(self, nickname: str) -> str:
        url = self.BASE_URL + f'gameArchives.jsp?user={nickname}'
        print(f'Downloading {url}')
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise Exception(response.text)
        return response.text
