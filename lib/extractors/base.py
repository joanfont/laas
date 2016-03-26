from lib.base import ParserMixin
from lib.entities import Lyrics, Song


class BaseExtractor(ParserMixin):

    @classmethod
    def extract(cls, song):

        if not isinstance(song, Song):
            raise AttributeError('song parameter must be a Song object')

        url = song.url
        raw_content = cls.get_raw_content(url)
        soup = cls.get_soup(raw_content)
        lyrics = cls.parse(soup)

        if not isinstance(lyrics, str):
            raise ValueError('parse() response must be a string')

        lyrics = cls.build_lyrics_object(lyrics, song)

        return lyrics

    @classmethod
    def build_lyrics_object(cls, lyrics, song):
        return Lyrics(lyrics, song)

    @classmethod
    def parse(cls, soup):
        raise NotImplementedError


