# Write your own tests for the housing.py file here.
# You must include the tests asked for in the assignment for full credit.
# You may add additional tests if you would like to test your code more thoroughly.
# Additional tests will not result in a higher grade.
# This file must be able to be run without error in order to receive credit for the required testing.
####
# Schrijf hier je eigen tests voor het housing.py bestand.
# Je moet de gevraagde tests in de opdracht opnemen voor volledige waardering.
# Je mag extra tests toevoegen als je je code grondiger wilt testen.
# Extra tests zullen niet leiden tot een hoger cijfer.
# Dit bestand moet zonder fouten uitgevoerd kunnen worden om punten te krijgen voor de vereiste testen.

from housing import Villa,StudentenKot 

import pytest

def setup_maximum_occupants():
    global studio,studio2,appartement
    studio = StudentenKot("Dorpsstraat 25",30)
    studio2 = StudentenKot("Dorpsstraat 26",40)
    appartement = Villa("lakenlaan 20",200,3,None)

def test_maximum_occupants():
    assert studio.maximum_occupants == 1
    assert studio2.maximum_occupants == 2
    assert appartement.maximum_occupants == 6