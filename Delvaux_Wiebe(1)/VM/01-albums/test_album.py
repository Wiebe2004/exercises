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

def test_create_black_cover():
    alors_on_dance = Song("SONG0001aaaa", "Alors on dance", 205)

    cd_chanson = CD("Chanson CD")
    cd_chanson.add_song(alors_on_dance)

    cd_chanson.create_back_cover()
    assert cd_chanson.create_back_cover == " Album: Chanson CD\nSensualité - 232s\n Alors on dance - 205s\n Ca plane pour moi - 182s"