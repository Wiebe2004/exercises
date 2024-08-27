from abc import ABC, abstractmethod
import re

class Util:
    @staticmethod
    def is_valid_track_id(track_id):
        return bool(re.fullmatch('TRK[0-9]{1}[0-9]{1}[1-8]{1}[A-Z]{2}[0-9]{2}',track_id))

class Track:
    def __init__(self, track_id, title,duration):
        if not Util.is_valid_track_id(track_id):
            raise ValueError(f"Track ID: {track_id} not valid.")
        self.title = title
        self.duration = duration
        self.__track_id = track_id
    
    @property
    def track_id(self):
        return self.__track_id
    
    @track_id.setter
    def track_id(self,track_id):
        if not Util.is_valid_track_id(track_id):
            raise ValueError(f"Track ID: {track_id} not valid.")
        else:
            self.__track_id = track_id
    

    def __str__(self):
        return f"Track: {self.title}, Duration: {self.duration}, Track ID: {self.track_id}"
    
class Album:
    def __init__(self, title, max_duration):
        self.title = title
        self.max_duration = max_duration
        self.__tracks = dict()
    
    @property
    def total_used_duration(self):
        return sum(track.duration for track in self.__tracks.values())
    
    @property
    def remaining_duration(self):
        return self.max_duration - self.total_used_duration
    
    def add_track(self,track):
        if track.duration > self.remaining_duration:
            raise RuntimeError("Not enough time left on the album")
        else:
            self.__tracks[track.track_id] = track
    
    def remove_track(self, track):
        if track in self.__tracks.values():
            self.__tracks.pop(track.track_id)
        else:
            raise RuntimeError("Track is not in Album")
    
    @property
    def track_titles(self):
        return [track.title for track in self.__tracks.values()]
    
    def sort_tracks_by_title(self):
        return sorted(self.__tracks.values(), key=lambda track: track.title) #VERGEET .VALUES() NIET
    
    @abstractmethod
    def generate_back_cover(self):
        ...

class Vinyl(Album):
    def __init__(self, title):
        super().__init__(title, max_duration = 2400)
    
    def generate_back_cover(self):
        back_cover = f"Album: {self.title}"
        self.__tracks = self.sort_tracks_by_title()
        for song in self.__tracks:
            back_cover += f"\n{song.title} - {song.duration}s"
        return back_cover

    def add_track(self, track):
        if not track.duration > 300:
            super().add_track(track)
        else:
            raise RuntimeError("Track is to long for this Vinyl")

class StreamingAlbum(Album):
    def __init__(self, title, description):
        super().__init__(title, max_duration=float('inf'))
        self.description = description

    def generate_back_cover(self):
        back_cover = f"Album: {self.title}\nDescription: {self.description}"
        self.__tracks = self.sort_tracks_by_title()
        for song in self.__tracks:
            back_cover += f"\n{song.title} - {song.duration}s"
        return back_cover

imagine = Track("TRK001AB12", "Imagine", 183)
let_it_be = Track("TRK002CD34", "Let it Be", 240)
hey_jude = Track("TRK003EF56", "Hey Jude", 431)
# invalid_track = Track("TRK999ZZ99", "Invalid Track", 120)
# ValueError: Invalid Track ID provided
yellow_submarine = Track("TRK004GH78", "Yellow Submarine", 145)

# Print Imagine
print(imagine)
# Track: "Imagine", Duration: 183, Track ID: TRK001AB12

# Create a vinyl album
beatles_vinyl = Vinyl("The Beatles Vinyl")

# Adding tracks to the vinyl album
beatles_vinyl.add_track(imagine)
beatles_vinyl.add_track(let_it_be)
# beatles_vinyl.add_track(hey_jude)
# RuntimeError: Tracks longer than 300 seconds cannot be added to a Vinyl
beatles_vinyl.add_track(yellow_submarine)

# Print track titles
print(beatles_vinyl.track_titles)
['Imagine', 'Let it Be', 'Yellow Submarine']

# Print Back Cover
print(beatles_vinyl.generate_back_cover())

# Create a streaming album
beatles_stream = StreamingAlbum("The Beatles Stream", "Stream all the hits from The Beatles!")

# Adding tracks to the streaming album
beatles_stream.add_track(imagine)
beatles_stream.add_track(let_it_be)
beatles_stream.add_track(hey_jude)
beatles_stream.add_track(yellow_submarine)

# Print the back cover
print(f'\n',beatles_stream.generate_back_cover())