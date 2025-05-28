class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1

        Song.genres.append(genre)
        Song.artists.append(artist)

        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_to_genres(cls):
        cls.genres = list(set(cls.genres))

    @classmethod
    def add_to_artists(cls):
        cls.artists = list(set(cls.artists))

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1