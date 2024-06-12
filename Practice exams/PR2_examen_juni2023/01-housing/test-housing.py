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
from housingSolution import Villa, StudentKot

import pytest

def setup_function():
    global villa1, studentenkot1, studentenkot2, studentenkot3, appartement1
    villa1 = Villa(None, 72, 3, None)
    studentenkot1 = StudentKot(None, 30)
    studentenkot2 = StudentKot(None, 40)
    appartement1 = Villa(None, 200, 3, None)
    
def test_maximum_residents():
    assert villa1.maximum_occupants == 3
    assert studentenkot1.maximum_occupants == 1
    assert studentenkot2.maximum_occupants == 2
    assert appartement1.maximum_occupants == 6 