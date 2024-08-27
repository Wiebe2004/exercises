# Write your own tests for the event.py file here.
# You must include the tests asked for in the assignment for full credit.
# You may add additional tests if you would like to test your code more thoroughly.
# Additional tests will not result in a higher grade.
# This file must be able to be run without error in order to receive credit for the required testing.
####
# Schrijf hier je eigen tests voor het event.py bestand.
# Je moet de gevraagde tests in de opdracht opnemen voor volledige waardering.
# Je mag extra tests toevoegen als je je code grondiger wilt testen.
# Extra tests zullen niet leiden tot een hoger cijfer.
# Dit bestand moet zonder fouten uitgevoerd kunnen worden om punten te krijgen voor de vereiste testen.
import pytest
from event import Artist, Festival, FreeConcert

@pytest.fixture
def setup_festival():
    festival = Festival("Test Festival", 2, 3, 5000, 20)  # 2 stages, 3 slots, 5000 attendees, ticket price 20
    return festival

def test_festival_profit_basic(setup_festival):
    # Arrange
    festival = setup_festival
    artist1 = Artist("SB123456AAAA", "Artist 1", 10000)
    artist2 = Artist("SB123456EEEE", "Artist 2", 5000)
    
    festival.add_artist(artist1)
    festival.add_artist(artist2)
    
    # Act
    profit = festival.calculate_profit()

    # Assert
    assert profit == (5000 * 20) - (10000 + 5000), "The profit should be 5000"

def test_festival_no_attendees(setup_festival):
    # Arrange
    festival = Festival("Empty Festival", 2, 3, 0, 20)  # 0 attendees
    artist = Artist("SB123456AAAA", "Artist 1", 10000)
    festival.add_artist(artist)
    
    # Act
    profit = festival.calculate_profit()
    
    # Assert
    assert profit == 0 - 10000, "The profit should be -10000 due to no revenue"

@pytest.fixture
def setup_free_concert():
    concert = FreeConcert("Test Free Concert", 3)  # 1 stage, 3 slots
    return concert

def test_free_concert_profit_basic(setup_free_concert):
    # Arrange
    concert = setup_free_concert
    artist1 = Artist("SB123456AAAA", "Artist 1", 5000)
    artist2 = Artist("SB123456EEEE", "Artist 2", 3000)
    
    concert.add_artist(artist1)
    concert.add_artist(artist2)
    
    # Act
    profit = concert.calculate_profit()

    # Assert
    assert profit == 0 - (5000 + 3000), "The profit should be -8000"

def test_free_concert_artist_wage_limit(setup_free_concert):
    # Arrange
    concert = setup_free_concert
    expensive_artist = Artist("SB123456IIII", "Expensive Artist", 15000)
    
    # Act & Assert
    with pytest.raises(RuntimeError, match="Artist's wage is too high for a FreeConcert."):
        concert.add_artist(expensive_artist)
