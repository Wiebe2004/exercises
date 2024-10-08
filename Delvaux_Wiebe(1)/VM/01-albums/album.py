import re
from abc import ABC, abstractmethod


class Util:
    @staticmethod
    def is_valid_song(song_id):
        return bool(re.fullmatch('SONG[0-2][0-9]{3}[aeiou]{4}', song_id))

class Song:
    def __init__(self, song_id,title,duration):
        if not Util.is_valid_song(song_id):
            raise ValueError("Invalid Song ID provided")
        self.title = title
        self.duration = duration
        self.song_id = song_id# MOET NIET ZOALS self.__song_id = song_id WANT DEZE SELF ROEPT DE PROPERTY OP

    @property
    def song_id(self):
        return self.__song_id  
    
    @song_id.setter
    def song_id(self,song_id):
        if not Util.is_valid_song(song_id):
            raise ValueError("Invalid Song ID provided")    
        self.__song_id = song_id
    
    def __str__(self):
        return f"Song: {self.title}, Duration: {self.duration}, Song ID: {self.__song_id}"
        

class Album:
    def __init__(self, name,total_duration):
        self.name = name
        self.total_duration = total_duration
        self.__songs = dict()

    @property
    def used_duration(self):
        return sum(song.duration for song in self.__songs.values())

    @property
    def available_duration(self):
        return self.total_duration - self.used_duration
    
    def add_song(self,song):
        if song.duration > self.available_duration:
            raise RuntimeError("Not enough available duration...")
        else:
            self.__songs[song.song_id] = song
    def remove_song(self,song):
        if song in self.__songs.values():
            self.__songs.pop(song.song_id)
        else:
            raise RuntimeError("Song was not found in Album")
        
    @property
    def song_titles(self):
        return [song.title for song in self.__songs.values()]
    
    def sort_songs_by_duration(self):
        return sorted(self.__songs.values(), key=lambda song: -song.duration )

    @abstractmethod
    def create_back_cover(self):
        ...

class DigitalAlbum(Album):
    def __init__(self, name, total_duration, credits):
        super().__init__(name, total_duration)
        self.credits = credits
    
    def create_back_cover(self):
        back_cover = f"Album: {self.name}\nCredits: {self.credits}"
        self.__songs = self.sort_songs_by_duration()
        for song in self.__songs:
            back_cover += f"\n{song.title} - {song.duration}s (ID: {song.song_id})"
        return back_cover
    
class CD(Album):
    def __init__(self, name):
        super().__init__(name, total_duration = 4320)
    
    def create_back_cover(self):
        back_cover = f"Album: {self.name}"
        self.__songs = self.sort_songs_by_duration()
        for song in self.__songs:
            back_cover += f"\n{song.title} - {song.duration}s (ID: {song.song_id})"
        return back_cover
    
    def add_song(self,song):
        if song.duration < 360:
            super().add_song(song)
        else:
            raise RuntimeError("Song duration cannot be longer then 360s")

# Create some songs
alors_on_dance = Song("SONG0001aaaa", "Alors on dance", 205)
la_tribu_de_dana = Song("SONG0002eeee", "La tribu de Dana", 224)
les_lac_du_connemara = Song("SONG1001aeio", "Les Lac du Connemara", 349)
# aline = Song("SONG3001abba", "Aline", 170)
ca_plane_pour_moi = Song("SONG1002oooo", "Ca plane pour moi", 182)
tout_oublier = Song("SONG2998aaaa", "Tout oublier", 202)
sensualite = Song("SONG2999uoie", "Sensualité", 232 )

# Print Alors On Dance
# print(ca_plane_pour_moi)
# Create an digitalalbum
french_songs = DigitalAlbum("French Songs", 1000, "This is a digital album, full of french songs")

# Adding songs to our digital album
french_songs.add_song(alors_on_dance)
french_songs.add_song(la_tribu_de_dana)
french_songs.add_song(les_lac_du_connemara)
french_songs.add_song(ca_plane_pour_moi)
# french_songs.add_song(tout_oublier)
french_songs.remove_song(ca_plane_pour_moi)
# french_songs.add_song(tout_oublier)
# french_songs.remove_song(ca_plane_pour_moi)

# Print song titles
# print(french_songs.song_titles)

# Print Back Cover
# print(french_songs.create_back_cover(), f"\n\n")

# Create a CD
cd_chanson = CD("Chanson CD")

# Adding songs to our CD
cd_chanson.add_song(alors_on_dance)
# cd_chanson.add_song(les_lac_du_connemara)
cd_chanson.add_song(la_tribu_de_dana)
cd_chanson.add_song(les_lac_du_connemara)

# Print the back cover
print(cd_chanson.create_back_cover())