import unittest
from PartA import Artist, Song, Album, Playlist


class TestClasses(unittest.TestCase):

    #test is instance class
    def test_artist_instance(self):
        artist = Artist("Taylor Swift", "2000-12-12", "USA")
        self.assertIsInstance(artist, Artist)

    def test_song_instance(self):
        song = Song("Love Story", "Taylor Swift", 2008)
        self.assertIsInstance(song, Song)

    def test_album_instance(self):
        album = Album("Fearless", "Taylor Swift", 2008)
        self.assertIsInstance(album, Album)

    def test_playlist_instance(self):
        playlist = Playlist("My Playlist")
        self.assertIsInstance(playlist, Playlist)

    # test is not instance class
    def test_artist_not_song(self):
        artist = Artist("Taylor Swift", "2000-12-12", "USA")
        self.assertNotIsInstance(artist, Song)

    def test_song_not_album(self):
        song = Song("Love Story", "Taylor Swift", 2008)
        self.assertNotIsInstance(song, Album)

    def test_album_not_playlist(self):
        album = Album("Fearless", "Taylor Swift", 2008)
        self.assertNotIsInstance(album, Playlist)

    def test_playlist_not_artist(self):
        playlist = Playlist("My Playlist")
        self.assertNotIsInstance(playlist, Artist)

    # test identity
    def test_identical_objects(self):
        song1 = Song("Style", "Taylor Swift", 2014)
        song2 = song1
        self.assertIs(song1, song2)

    def test_non_identical_but_similar_objects(self):
        song1 = Song("Style", "Taylor Swift", 2014)
        song2 = Song("Style", "Taylor Swift", 2014)
        self.assertIsNot(song1, song2)

    # test add_song & add_album
    def test_album_add_song(self):
        album = Album("Red", "Taylor Swift", 2012)
        song = album.add_song("22", 2012)
        self.assertIn(song, album.songs)

    def test_artist_add_song(self):
        artist = Artist("Taylor Swift", "2000-12-12", "USA")
        song = Song("22", "Taylor Swift", 2012)
        artist.add_song(song)
        self.assertIn(song, artist.songs)

    def test_artist_add_album(self):
        artist = Artist("Taylor Swift", "2000-12-12", "USA")
        album = Album("Red", "Taylor Swift", 2012)
        artist.add_album(album)
        self.assertIn(album, artist.albums)

    def test_playlist_add_song(self):
        playlist = Playlist("My Playlist")
        song = Song("22", "Taylor Swift", 2012)
        playlist.add_song(song)
        self.assertIn(song, playlist.songs)


    # sort & shuffle
    def test_sort_playlist_ascending(self):
        playlist = Playlist("Test")
        s1 = Song("B Song", "Artist", 2020)
        s2 = Song("A Song", "Artist", 2020)

        playlist.add_song(s1)
        playlist.add_song(s2)

        playlist.sort_playlist('ASC')

        self.assertEqual(playlist.songs[0].title, "A Song")

    def test_sort_playlist_descending(self):
        playlist = Playlist("Test")
        s1 = Song("B Song", "Artist", 2020)
        s2 = Song("A Song", "Artist", 2020)

        playlist.add_song(s1)
        playlist.add_song(s2)

        playlist.sort_playlist('DES')

        self.assertEqual(playlist.songs[0].title, "B Song")

    def test_shuffle_playlist(self):
        playlist = Playlist("Test")
        s1 = Song("A", "Artist", 2020)
        s2 = Song("B", "Artist", 2020)
        s3 = Song("C", "Artist", 2020)

        playlist.add_song(s1)
        playlist.add_song(s2)
        playlist.add_song(s3)

        original_order = playlist.songs.copy()
        playlist.shuffle_playlist()

        self.assertCountEqual(playlist.songs, original_order)


if __name__ == "__main__":
    unittest.main()