import re
from abc import ABC, abstractmethod

class Util:
    @staticmethod
    def is_valid_sabam_id(sabam_id):
        pattern = r'^SB\d{6}[AEIOU]{4}$'
        return bool(re.match(pattern, sabam_id))

class Artist:
    def __init__(self, sabam_id, name, wage):
        if not Util.is_valid_sabam_id(sabam_id):
            raise ValueError(f"Invalid SABAM ID: {sabam_id}")
        self.name = name
        self.wage = wage
        self._sabam_id = sabam_id

    @property
    def sabam_id(self):
        return self._sabam_id

    @sabam_id.setter
    def sabam_id(self, value):
        if not Util.is_valid_sabam_id(value):
            raise ValueError(f"Invalid SABAM ID: {value}")
        self._sabam_id = value

    def __str__(self):
        return f'Artist: {self.name}, Wage: {self.wage}, Sabam ID: {self._sabam_id}'


class Event(ABC):
    def __init__(self, name, number_of_stages, number_of_slots):
        self.name = name
        self.number_of_stages = number_of_stages
        self.number_of_slots = number_of_slots
        self._artists = {}

    @property
    def number_of_artists(self):
        return len(self._artists)

    @property
    def maximum_artists(self):
        return self.number_of_stages * self.number_of_slots

    def add_artist(self, artist):
        if self.number_of_artists >= self.maximum_artists:
            raise RuntimeError("Cannot add artist: Maximum number of artists reached.")
        self._artists[artist.sabam_id] = artist

    def remove_artist(self, artist):
        if artist.sabam_id not in self._artists:
            raise RuntimeError("Cannot remove artist: Artist not found.")
        del self._artists[artist.sabam_id]

    @property
    def sum_wages_of_artists(self):
        return sum(artist.wage for artist in self._artists.values())

    def sort_artists_by_name(self):
        return sorted(self._artists.values(), key=lambda artist: artist.name)

    @abstractmethod
    def calculate_profit(self):
        pass

class Festival(Event):
    def __init__(self, name, number_of_stages, number_of_slots, number_of_attendees, ticket_price):
        super().__init__(name, number_of_stages, number_of_slots)
        self.number_of_attendees = number_of_attendees
        self.ticket_price = ticket_price

    def calculate_profit(self):
        revenue = self.number_of_attendees * self.ticket_price
        costs = self.sum_wages_of_artists
        return revenue - costs

class FreeConcert(Event):
    def __init__(self, name, number_of_slots):
        super().__init__(name, 1, number_of_slots)  # number_of_stages is always 1

    def calculate_profit(self):
        revenue = 0
        costs = self.sum_wages_of_artists
        return revenue - costs

    def add_artist(self, artist):
        if artist.wage >= 10000:
            raise RuntimeError("Artist's wage is too high for a FreeConcert.")
        super().add_artist(artist)

# creating some artists
rihanna = Artist("SB123456AAAA", "Rihanna", 20000)
metallica = Artist("SB123456EEEE", "Metallica", 30000)
pommelien = Artist("SB123456OOOO", "Pommelien Thijs", 5000)
samson = Artist("SB123456IIII", "Samson en Gert", 8000)
elton = Artist("SB123456UUUU", "Elton John", 22000)
elvis = Artist("SB123455AAAA", "Elvis Presley", 50000)

print(rihanna)
# creating a Festival
rock_werchter = Festival("Rock Werchter", 1, 2, 10000, 10)

# adding some artists to the festival
rock_werchter.add_artist(metallica)
rock_werchter.add_artist(rihanna)

rock_werchter.remove_artist(rihanna)
rock_werchter.add_artist(samson)


# Print Artist names sorted
sorted_artists = rock_werchter.sort_artists_by_name()
for artist in sorted_artists:
    print(artist)

# calculating the profit of Rock Werchter
print(rock_werchter.calculate_profit())


# creating a FreeConcert
rock_blanden = FreeConcert("Rock Blanden", 1)

# adding some artists to Rock Blanden

rock_blanden.add_artist(pommelien)

# calculating the profit (loss) of Rock Blanden
print(rock_blanden.calculate_profit())
