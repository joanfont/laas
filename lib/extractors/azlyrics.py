from lib.extractors.base import BaseExtractor


class Extractor(BaseExtractor):

    @classmethod
    def parse(cls, soup):
        song_div = soup.find('div', {'class': None, 'id': None})
        return song_div.text
