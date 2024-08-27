# Write your own tests for the album.py file here.
# You must include the tests asked for in the assignment for full credit.
# You may add additional tests if you would like to test your code more thoroughly.
# Additional tests will not result in a higher grade.
# This file must be able to be run without error in order to receive credit for the required testing.
####
# Schrijf hier je eigen tests voor het album.py bestand.
# Je moet de gevraagde tests in de opdracht opnemen voor volledige waardering.
# Je mag extra tests toevoegen als je je code grondiger wilt testen.
# Extra tests zullen niet leiden tot een hoger cijfer.
# Dit bestand moet zonder fouten uitgevoerd kunnen worden om punten te krijgen voor de vereiste testen.
import pytest
from album import DigitalAlbum, CD, Song

def songs():
    return [Song("SONG0001aaaa", "Ik ben de man", 205),
     Song("SONG0002eeee", "Smurfenlied", 224),
     Song("SONG1001aeio", "Kaboutersquad", 354)
    ]

def name():
    return "Dutch songs"

def credits():
    return "This is an album of my favourite dutch songs"


def test_back_cover_of_DigitalAlbum():
    test_name = name()
    test_album = DigitalAlbum(test_name, 10000, credits())
    test_songs = songs()
    for song in test_songs:
        test_album.add_song(song)
    back_cover = "Album: Dutch songs\nCredits: This is an album of my favourite dutch songs\nSong: Kaboutersquad, Duration: 354, Song ID: SONG1001aeio\nSong: Smurfenlied, Duration: 224, Song ID: SONG0002eeee\nSong: Ik ben de man, Duration: 205, Song ID: SONG0001aaaa\n"
    assert test_album.create_back_cover() == back_cover

def test_back_cover_of_cd():
    test_name = name()
    test_album = CD(test_name)
    test_songs = songs()
    for song in test_songs:
        test_album.add_song(song)
    back_cover = "Album: Dutch songs\nSong: Kaboutersquad, Duration: 354, Song ID: SONG1001aeio\nSong: Smurfenlied, Duration: 224, Song ID: SONG0002eeee\nSong: Ik ben de man, Duration: 205, Song ID: SONG0001aaaa\n"
    assert test_album.create_back_cover() == back_cover
