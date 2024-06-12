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
from housing import Residence
from housing import Villa
import pytest
import math

@pytest.mark.parametrize('area, number_of_rooms', [
    (21, 1),
    (33, 1),
    (45, 2),
    (88, 1),
    (0, 0),
    (158, 10),
    (89, 4), 
    (123, 9)
])

def test_residence(area, number_of_rooms):
    actual = Villa('Leuven', area, number_of_rooms, 3).maximum_occupants
    assert min((math.floor(area/20), number_of_rooms * 2)) == actual

