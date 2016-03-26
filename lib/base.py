import requests
from bs4 import BeautifulSoup


class ParserMixin:

    BASE_URL = None

    @classmethod
    def get_raw_content(cls, url):
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        })
        return response.content

    @classmethod
    def get_soup(cls, raw_content):
        return BeautifulSoup(raw_content, 'lxml')


