import re
from abc import ABC, abstractmethod

class Util:
    @staticmethod
    def is_valid_sabam_id(sabam_id):
        return bool(re.fullmatch("SB[0-9]{6}[AEIOU]{4}", sabam_id))

class Artist:
    def __init__(self, sabam_id,name,wage):
        if not Util.is_valid_sabam_id(sabam_id):
            raise ValueError("Not a valid sabam ID")
        self.name = name
        self.wage = wage
        self.sabam_id = sabam_id # MOET NIET ZOALS self.__sabam_id = sabam_id WANT DEZE SELF ROEPT DE PROP OP

    @property
    def sabam_id(self):
        return self.__sabam_id

    @sabam_id.setter
    def sabam_id(self,sabam_id):
        if not Util.is_valid_sabam_id(sabam_id):
            raise ValueError("Not a valid sabam ID")
        else:
            self.__sabam_id = sabam_id
    
    def __str__(self):
        return f"Artist: {self.name}, Wage: {self.wage}, Sabam ID: {self.sabam_id}"
    
class Event(ABC):
    def __init__(self, name,number_of_stages,number_of_slots):
        self.name = name
        self.number_of_stages = number_of_stages
        self.number_of_slots = number_of_slots
        self.__artists = dict()

    @property
    def number_of_artists(self):
        return len(self.__artists)
    
    @property
    def maximum_artists(self):
        return self.number_of_stages*self.number_of_slots
    
    def add_artist(self, artist):
        if self.number_of_artists == self.maximum_artists:
            raise RuntimeError("Line-up Full. Cannot add artist")
        else:
            self.__artists[artist.sabam_id] = artist
    
    def remove_artist(self, artist):
        if artist not in self.__artists.values():
            raise RuntimeError("Cannot delete artist that doesnt exist")
        else:
            self.__artists.pop(artist.sabam_id)

    @property
    def sum_wages_of_artists(self):
        return sum(artist.wage for artist in self.__artists.values())
    
    def sort_artists_by_name(self):
        return sorted(self.__artists.values(), key=lambda artist: artist.name) #Check of het alfabetisch is.
    
    @abstractmethod
    def calculate_profit():
        ...

class Festival(Event):
    def __init__(self, name, number_of_stages, number_of_slots,number_of_attendees,ticket_price):
        super().__init__(name, number_of_stages, number_of_slots)
        self.number_of_attendees = number_of_attendees
        self.ticket_price = ticket_price
    
    def calculate_profit(self):
        profit = self.number_of_attendees * self.ticket_price
        costs = self.sum_wages_of_artists
        return profit - costs
         
    
class FreeConcert(Event):
    def __init__(self, name, number_of_slots):
        super().__init__(name, 1,number_of_slots)

    def calculate_profit(self):
        costs = self.sum_wages_of_artists
        return 0 - costs
        

    def add_artist(self, artist):
        if artist.wage > 10000:
            return RuntimeError("Cannot add artists with wages higher then 10.000 euros")
        else:
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
