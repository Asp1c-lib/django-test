import random



class Artist:
    def __init__(self, name, DoB, country):
        self.name = name
        self.DoB = DoB
        self.country = country
        self.albums = []
        self.songs = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)

    def display_info(self):
        print("-------------------------------")
        print(f"Artist Name: {self.name}, DoB: {self.DoB}, Country: {self.country}")
        print("Albums:", [album.title for album in self.albums])
        print("Songs:", [song.title for song in self.songs])
        print("-------------------------------")
        
        
        
class Song:
    def __init__(self, title, artist_name, year):
        self.title = title
        self.artist_name = artist_name
        self.year = year

    def display_info(self):
        print("-------------")
        print(f"Song Title: {self.title}, Artist: {self.artist_name}, Year: {self.year}")
        print("-------------")



class Album:
    def __init__(self, title, artist_name, year):
        self.title = title
        self.artist_name = artist_name
        self.year = year
        self.songs = []

    def add_song(self, title, year):
        song = Song(title, self.artist_name, year)
        self.songs.append(song)
        return song

    def display_info(self):
        print("-------------------------------")
        print(f"Album Title: {self.title}, Artist: {self.artist_name}, Year: {self.year}")
        print("Songs:", [song.title for song in self.songs])
        print("-------------------------------")




class Playlist:
    def __init__(self, title):
        self.title = title
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def print_all_song(self):
        print("-------------------------------")
        print(f"Playlist: {self.title}")
        for song in self.songs:
            song.display_info()
        print("-------------------------------")

    def sort_playlist(self, order='ASC'):
        reverse = False
        if order == 'DES':
            reverse = True
        elif order != 'ASC':
            print("Invalid, use 'ASC' or 'DES' ")
            
        self.songs.sort(key=lambda song: song.title, reverse=reverse)
        
    def shuffle_playlist(self):
        random.shuffle(self.songs)
        
        
if __name__ == "__main__":
    #Create an artist
    artist = Artist("Taylor Swift", "2000-12-12", "USA")

    #Create an album
    album = Album("Fearless", "Taylor Swift", 2000)

    #Create a few songs for the artist you have created
    s1 = Song("Tim McGraw", "Taylor Swift", 2001)
    s2 = Song("Picture To Burn", "Taylor Swift", 2002)
    s3 = Song("Teardrops On My Guitar", "Taylor Swift", 2003)
    s4 = Song("A Place In This World", "Taylor Swift", 2004)


    #Use method add_song() from the Album class to add two songs
    s5 = album.add_song("Fearless", 2005)
    s6 = album.add_song("Fifteen", 2006)

    #Use methods add_album() and add_song() to update the information of the artist
    artist.add_album(album)

    artist.add_song(s1)
    artist.add_song(s2)

    #display artist info
    artist.display_info()

    #display album info
    album.display_info()

    #Create a playlist
    playlist = Playlist("Taylor Swift Playlist")

    #Add all songs from the album to the playlist
    for song in album.songs:
        playlist.add_song(song)
        
    #added more song to better see later
    playlist.add_song(s1)
    playlist.add_song(s2)

        
    #print normal playlist
    print("\n Normal Playlist:")
    playlist.print_all_song()

    #sort playlist ASC
    playlist.sort_playlist('ASC')
    print("\n Sorted Playlist (ASC):")
    playlist.print_all_song()

    #sort playlist DES
    playlist.sort_playlist('DES')
    print("\n Sorted Playlist (DES):")
    playlist.print_all_song()

    #shuffle playlist
    playlist.shuffle_playlist()
    print("\n Shuffled Playlist:")
    playlist.print_all_song()