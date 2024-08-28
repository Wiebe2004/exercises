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

from housing import *

def test_maximum_occupants_kot():
    test_kot = StudentKot("Kortestraat 6, 3000 Leuven",20)
    kot_value = test_kot.calculate_value()
    test_value = 150000+(750*test_kot.area) 
    assert kot_value == test_value

def test_maximum_occupants_villa():
    test_villa = Villa("Roeselbergdal 44, 3012 Wilsele", 151, 4, 1)
    villa_value = test_villa.calculate_value()
    test_value = (25000*test_villa.number_of_rooms) + (2100*test_villa.area) + (10000*test_villa.garage_capacity)
    assert villa_value == test_value

# Kan misschien ook zoals eerdere testen de eerste testen, check deze indien tijd over. 