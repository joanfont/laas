from urllib.parse import urlencode

from lib.entities import Song
from lib.seekers.base import BaseSeeker


class Seeker(BaseSeeker):
    @classmethod
    def parse(cls, soup):
        results_table = soup.find('table', {'class': 'table table-condensed'})
        result_items = results_table.find_all('td')
        songs = map(cls.parse_item, result_items)
        return list(songs)

    @classmethod
    def parse_item(cls, td):
        td_link = td.find('a')
        title, artist = cls.get_title_and_artist_from_td(td)
        url = td_link.get('href')
        return Song(title, artist, url)

    @classmethod
    def get_title_and_artist_from_td(cls, td):
        bold_items = td.find_all('b')
        if len(bold_items) >= 2:
            song, artist, *_ = bold_items
            return song.text, artist.text
        else:
            return None, None

    @classmethod
    def get_url(cls, query):
        query_string = urlencode({
            'q': query
        })
        return 'http://search.azlyrics.com/search.php?{query_string}'.format(query_string=query_string)
