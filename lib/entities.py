
class BaseEntity:
    def to_dict(self):
        raise NotImplementedError


class Lyrics(BaseEntity):
    def __init__(self, lyrics, song):
        self.lyrics = lyrics
        self.song = song

    def to_dict(self):
        return {
            'song': self.song.to_dict(),
            'lyrics': self.lyrics
        }

    def __repr__(self):
        return self.song


class Song(BaseEntity):
    def __init__(self, title, artist, url):
        self.title = title
        self.artist = artist
        self.url = url

    def to_dict(self):
        return {
            'title': self.title,
            'artist': self.artist,
        }

    def __repr__(self):
        return '{title} - {artist}'.format(title=self.title, artist=self.artist)
