import re
from abc import ABC, abstractmethod


class Util:
    @staticmethod
    def is_valid_song_id(song_id):
        return bool(re.fullmatch(r"w\{12}^SONG[0000-2999][aeiou]$", song_id))


class Song:
    def __init__(self, song_id, title, duration):

        self.title = title
        self.duration = duration
        self.__song_id = song_id

    @property
    def song_id(self):
        return self.__song_id

    @song_id.setter
    def song_id(self, song_id):
        self.__song_id = song_id

    def __str__(self):
        return (
            f"Song: {self.title}, Duration: {self.duration}, Song ID: {self.__song_id}"
        )


class Album(ABC):
    def __init__(self, name, total_duration):
        self.name = name
        self.total_duration = total_duration
        self.__songs = {}

    @property
    def songs(self):
        return self.__songs

    @property
    def used_duration(self):
        return self.total_duration

    @property
    def available_duration(self):
        return (self.used_duration) - (self.total_duration)

    def add_song(self, song):
        if self.used_duration >= self.total_duration:
            raise RuntimeError("Not enough available duration to add this song")
        else:
            self.__songs[song.id] = song

    def remove_song(self, song):
        if song.id in self.__songs:
            del self.__songs[id]
        else:
            raise RuntimeError("Song not found")

    @property
    def song_titles(self):
        return [song.name for song in self.__songs.values()]

    def __lt__(self, other):
        return self.used_duration < other.used_duration

    def sort_songs_by_duration(self):
        # self.__songs.sort()
        pass

    @property
    @abstractmethod
    def create_back_cover(self):
        pass


class DigitalAlbum(Album):
    def __init__(self, name, total_duration, credits):
        super().__init__(name, total_duration)
        self.credits = credits

    def create_back_cover(self):
        return f"Album: {self.name}, Credits: {self.credits},  "


class CD(Album):
    def __init__(self, name, total_duration):
        super().__init__(name, total_duration)
        self.total_duration = 4320

    def create_back_cover(self):
        return f"Album: {self.name}"

    def add_song(self, song):
        if self.used_duration >= 360:
            raise RuntimeError("Songs longer than 360 seconds cannot be added to a CD")
        else:
            super().add_song(song)
