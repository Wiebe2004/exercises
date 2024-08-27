# enter your code here to solve the album assignment
# voer hier je code in om de albumvraag op te lossen
from abc import ABC,abstractmethod
import re
class Util:
    @staticmethod
    def is_valid_song_id(song_id):
        if re.fullmatch("(SONG+(0-9){1,4}+(a|e|i|o|u)){1,12}",song_id):
            return True
        else:
            return False

class Song:
    def __init__(self,song_id,title,duration):
        if not Util.is_valid_song_id(song_id):
            raise ValueError("Song not valid")
        self.title = title
        self.duration = duration
        self.__song_id = song_id

    @property
    def song_id(self):
        return self.__song_id
    
    @song_id.setter
    def song_id(self,song_id):
        self.__song_id = song_id

    def __str__(self) -> str:
        return "Song:" + self.title + ", Duration: "+self.duration+", Song ID: "+self.song_id

class Album(ABC):
    def __init__(self,name,total_duration):
        self.name = name
        self.total_duration = total_duration
        self.__songs = {}

    @property
    def used_duration(self):
        used_duration = 0
        for song in self.__songs:
            used_duration+= song.duration
        return used_duration

    @property
    def available_duration(self):
        return self.used_duration-self.total_duration
    
    def add_song(self,song):
        if song.song_id in self.__songs:
            return
        elif self.song.duration > self.available_duration:
            raise RuntimeError("Not enough available duration")
        else:
            self.__songs[song.song_id] = song

    def remove_song(self,song):
        if song.song_id in self.__songs:
            del self.__songs[song.song_id]
        else:
            raise RuntimeError("Song is not in dictionary")

    @property
    def song_titles(self):
        return [song.title for song in self.__songs]

    def sort_songs_by_duration(self):
        return sorted(self.__songs, key=lambda song: -song.duration)

    @abstractmethod
    def create_back_cover(self):
        ...

class DigitalAlbum(Album):
    def __init__(self, name, total_duration,credits):
        super().__init__(name, total_duration)
        self.credits = credits

    def create_back_cover(self): 
        return [self.name,self.credits,self.sort_songs_by_duration()] #MSS ZOALS DE REPR
    
class CD(Album):
    def __init__(self, name):
        super().__init__(name,4320)

    def create_back_cover(self):
        return[self.name, self.sort_songs_by_duration()]
    
    def add_song(self, song):
        if song.duration > 360:
            raise RuntimeError("Duration cannot be longer then 360sec")
        else:
            super().add_song(song)
            
alors_on_dance = Song("SONG0001aaaa", "Alors on dance", 205)
la_tribu_de_dana = Song("SONG0002eeee", "La tribu de Dana", 224)
les_lac_du_connemara = Song("SONG1001aeio", "Les Lac du Connemara", 364)
aline = Song("SONG3001abba", "Aline", 170)
ca_plane_pour_moi = Song("SONG1002oooo", "Ca plane pour moi", 182)
tout_oublier = Song("SONG2998aaaa", "Tout oublier", 202)
sensualite = Song("SONG2999uoie", "Sensualité", 232 )
print(alors_on_dance)

french_songs = DigitalAlbum("French Songs", 1000, "This is a digital album, full of french songs")

french_songs.add_song(alors_on_dance)
french_songs.add_song(la_tribu_de_dana)
french_songs.add_song(les_lac_du_connemara)
french_songs.add_song(ca_plane_pour_moi)
french_songs.add_song(tout_oublier)

french_songs.remove_song(ca_plane_pour_moi)
french_songs.add_song(tout_oublier)
french_songs.remove_song(ca_plane_pour_moi)

print(french_songs.song_titles)

print(french_songs.create_back_cover())

cd_chanson = CD("Chanson CD")

cd_chanson.add_song(alors_on_dance)
cd_chanson.add_song(les_lac_du_connemara)
cd_chanson.add_song(ca_plane_pour_moi)
cd_chanson.add_song(sensualite)

print(cd_chanson.create_back_cover())