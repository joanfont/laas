from lib.base import ParserMixin
from lib.entities import Song
from lib.helper import Helper


class BaseSeeker(ParserMixin):

    @classmethod
    def seek(cls, query):
        url = cls.get_url(query)
        raw_content = cls.get_raw_content(url)
        soup = cls.get_soup(raw_content)

        songs = cls.parse(soup)

        if not Helper.array_of(songs, Song):
            raise ValueError('parse() response must be an array of Song objects')

        return songs

    @classmethod
    def parse(cls, soup):
        raise NotImplementedError

    @classmethod
    def get_url(cls, query):
        raise NotImplementedError
