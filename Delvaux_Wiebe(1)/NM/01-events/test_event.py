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
from event import Artist, Festival, FreeConcert

def ArtistsFestival():
    return [Artist("SB123456AAAA", "Rihanna", 20000),
            Artist("SB123456EEEE", "Metallica", 30000),
            Artist("SB123456OOOO", "Pommelien Thijs", 5000)
        ]

def ArtistsFreeConcert():
    return [Artist("SB123456OOOO", "Pommelien Thijs", 5000),
            Artist("SB123456IIII", "Samson en Gert", 8000),
            Artist("SB123445AEIO", "Average Rob", 2000)]

def name():
    return "Rock Werchter"

def test_calculate_profit_festival():
    test_Festival = Festival(name(),1, 3, 10000, 10)

    total_wage = 0
    for artist in ArtistsFestival():
        test_Festival.add_artist(artist) 
        total_wage += artist.wage
    profit = test_Festival.number_of_attendees*test_Festival.ticket_price
    winnings = test_Festival.calculate_profit()
    assert winnings == (profit - total_wage)

def test_calculate_profit_freeconcert():
    test_Festival = FreeConcert(name(),3)

    total_wage = 0
    for artist in ArtistsFreeConcert():
        test_Festival.add_artist(artist) 
        total_wage += artist.wage
    winnings = test_Festival.calculate_profit()
    assert winnings == (0 - total_wage)