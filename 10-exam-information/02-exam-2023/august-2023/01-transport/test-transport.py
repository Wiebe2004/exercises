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
import pytest
from transport import Passenger, Taxi, Bus

def test_passenger_name_validation():
    with pytest.raises(ValueError):
        Passenger("1", "Rihanna", 100)

def test_taxi_pickup():
    taxi = Taxi("ABC123", 4)
    passenger1 = Passenger("1", "Harry Styles", 50)
    passenger2 = Passenger("2", "Machine Gun Kelly", 30)
    taxi.pickup([passenger1, passenger2], 4)
    assert taxi.number_of_occupants == 2

def test_bus_boarding():
    bus = Bus("XYZ789", 10)
    passenger = Passenger("3", "John Doe", 5)
    bus.board(passenger)
    assert bus.number_of_occupants == 1
    assert passenger.money == 3