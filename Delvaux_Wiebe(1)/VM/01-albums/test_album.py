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

from album import *

#Eerst parameters van alle functies maken.
#Parameter die meegegeven word aan class SONG
def create_songs():
    return [Song("SONG0001aaaa", "Alors on dance", 205),
    Song("SONG0002eeee", "La tribu de Dana", 224),
    Song("SONG1001aeio", "Les Lac du Connemara", 349)
    ]

#Parameter die meegegeven word aan 
def name():
    return "French Songs"

def credits():
    return "La douce France"

def test_create_back_cover_of_CD():
    test_name = name()
    cd_french_songs = CD(test_name)
    test_songs = create_songs()
    for song in test_songs:
        cd_french_songs.add_song(song)
    back_cover = f"Album: {test_name}\nLes Lac du Connemara - 349s (ID: SONG1001aeio)\nLa tribu de Dana - 224s (ID: SONG0002eeee)\nAlors on dance - 205s (ID: SONG0001aaaa)"
    assert back_cover == cd_french_songs.create_back_cover()

def test_create_back_cover_of_DigitalAlbum():
    test_name = name()
    test_credits = credits()
    test_Album = DigitalAlbum(test_name,10000, test_credits)
    test_songs = create_songs()
    for song in test_songs:
        test_Album.add_song(song)
    back_cover = f"Album: {test_name}\nCredits: {test_credits}\nLes Lac du Connemara - 349s (ID: SONG1001aeio)\nLa tribu de Dana - 224s (ID: SONG0002eeee)\nAlors on dance - 205s (ID: SONG0001aaaa)"
    assert test_Album.create_back_cover() == back_cover