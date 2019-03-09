import requests
from ratelimit import limits
from ratelimit import sleep_and_retry
from requests import Response


class KGSClient:
    BASE_URL = 'https://www.gokgs.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 '
                      '(KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17',
    }

    def download_month_archive(self, nickname: str, year: int, month: int) -> bytes:
        url = self.BASE_URL + f'servlet/archives/ru_RU/{nickname}-{year}-{month}.zip'
        return self.request_kgs(url).content

    def get_archives_page(self, nickname: str) -> str:
        url = self.BASE_URL + f'gameArchives.jsp?user={nickname}'
        return self.request_kgs(url).text

    @sleep_and_retry
    @limits(calls=1, period=15)
    def request_kgs(self, url: str) -> Response:
        print(f'GET {url}')
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise Exception(f'Error {response.status_code}')
        return response
