# enter your code here to solve the transporation assignment
# voer hier je code in om de vervoersvraag op te lossen
from abc import ABC, abstractmethod
import re


class Passenger:
    @staticmethod
    def is_valid_name(name):
        return re.fullmatch(r"\w+\s\w+(\s\w+)*", name)
    
    def __init__(self, id, name, money):
        self.id = id
        self.money = money
        self.__name = name
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if not self.is_valid_name(new_name):
            raise ValueError("Name is not valid.")
        self.__name = new_name
        
class Vehicle(ABC):
    def __init__(self, license_plate, amount_of_seats):
        self.license_plate = license_plate
        self.amount_of_seats = amount_of_seats
        self.__occupants = {}
    
    @property
    def number_of_occupants(self):
        return len(self.__occupants)

    @property
    @abstractmethod
    def maximum_occupants(self):
        ...
        
    def add_passenger(self, passenger):
        if passenger.id in self.__occupants.keys():
            raise KeyError("Passenger already registered.")
        self.__occupants[passenger] = None
        
    def remove_passenger(self, passenger):
        if passenger not in self.__occupants.keys():
            raise ValueError("Person not found")
        self.__occupants.pop(passenger)
            
    def remove_all_passengers(self):
        for key in self.__occupants.keys():
            self.__occupants.pop(key)

    @property
    def occupant_names(self):
        return [passenger.name for passenger in self.__occupants.keys()]

class Taxi(Vehicle):
    def __init__(self, license_plate, amount_of_seats):
        super().__init__(license_plate, amount_of_seats)
        self.is_available = True
        
    @property
    def maximum_occupants(self):
        return 1
    
    def pickup(self, passengers, distance):
        responsible_passenger = passengers[0]
        total = 1 + distance
        if total < 5:
            total += 5 - total 
        if not self.is_available or len(passengers) > self.maximum_occupants:
            raise ValueError("Taxi is not available")
        if responsible_passenger.money < total:
            raise RuntimeError("Responsible passenger doesn't have enough money.")
        responsible_passenger.money -= total
        for passenger in passengers:
            self.add_passenger(passenger)
        self.is_available = False
        
    def dropoff(self):
        self.remove_all_passengers()
        self.is_available = True
        
class Bus(Vehicle):
    def __init__(self, license_plate, amount_of_seats):
        super().__init__(license_plate, amount_of_seats)
    
    @property
    def maximum_occupants(self):
        return 2 * self.amount_of_seats
    
    def board(self, passenger):
        total = 2
        if self.number_of_occupants >= self.maximum_occupants:
            raise ValueError("Vehicle is full")
        
        if passenger.money < total:
            raise RuntimeError
        passenger.money -= total
        self.add_passenger(passenger)
        
    def disembark(self, passenger):
        self.remove_passenger(passenger)
                         
aimee = Passenger("12.34.56-789.01", "Aimee Backiel", 40)
bastian = Passenger("01.02.03-040.05", "Bastian Li Backiel", 5)

mijn_taxi = Taxi("1-NGL-760", 4)
mijn_bus = Bus("1-HUE-344", 30)

mijn_bus.board(aimee)
mijn_bus.board(bastian)

print(mijn_bus.occupant_names)

mijn_bus.disembark(aimee)
mijn_bus.disembark(bastian)

print(mijn_bus.occupant_names)

mijn_bus.board(bastian)

mijn_taxi.pickup([aimee], 5)

print(mijn_bus.occupant_names)

print(mijn_taxi.occupant_names)

print(aimee.money)

print(bastian.money)

