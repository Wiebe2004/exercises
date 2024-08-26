import re
from abc import ABC, abstractmethod


class Util:
    @staticmethod
    def is_valid_song_id(song_id):
        return bool(re.fullmatch(r'SONG[0-2][0-9]{3}[aeiou]{4}', song_id))

class Song:
    def __init__(self, song_id, title, duration):
        if not Util.is_valid_song_id(song_id):
            raise ValueError("Invalid Song ID provided")
        self.title = title
        self.duration = duration
        self.__song_id = song_id

    @property
    def song_id(self):
        return self.__song_id
    
    @song_id.setter
    def song_id(self, song_id):
        if not Util.is_valid_song_id(song_id):
            raise ValueError("Invalid Song ID provided")
        self.__song_id = song_id

    def __str__(self):
        return f"Song: {self.title}, Duration: {self.duration}, Song ID: {self.__song_id}"

class Album(ABC):
    def __init__(self, name, total_duration):
        self.name = name
        self.total_duration = total_duration
        self.__songs = dict()

    @property
    def used_duration(self):
        return sum(song.duration for song in self.__songs.values())
    
    @property
    def available_duration(self):
        return self.total_duration - self.used_duration
    
    def add_song(self, song):
        if self.available_duration < song.duration:
            raise RuntimeError("Not enough available duration to add this song")
        self.__songs[song.song_id] = song

    def remove_song(self, song):
        if song not in self.__songs.values():
            raise RuntimeError("Song not found in album")
        self.__songs.pop(song.song_id)

    @property
    def song_titles(self):
        return [song.title for song in self.__songs.values()]
    
    def sort_songs_by_duration(self):
        return sorted(self.__songs.values(), key=lambda song: -song.duration)
    
    @abstractmethod
    def create_back_cover(self):
        ...

class DigitalAlbum(Album):
    def __init__(self, name, total_duration, credits):
        super().__init__(name, total_duration)
        self.credits = credits
    
    def create_back_cover(self):
        back_cover = f"Album: {self.name}\nCredits: {self.credits}\n"
        self.__songs = self.sort_songs_by_duration()
        for song in self.__songs:
            back_cover += str(song)
            back_cover += "\n"
        return back_cover
    
class CD(Album):
    def __init__(self, name):
        super().__init__(name, 4320)

    def create_back_cover(self):
        self.__songs = self.sort_songs_by_duration()
        back_cover = f"Album: {self.name}\n"
        for song in self.__songs:
            back_cover += str(song)
            back_cover += "\n"
        return back_cover

    def add_song(self, song):
        if song.duration > 360:
            raise RuntimeError("Songs longer than 360 seconds cannot be added to a CD")
        super().add_song(song)