# enter your code here to solve the transporation assignment
# voer hier je code in om de vervoersvraag op te lossen
from abc import ABC, abstractmethod

class Passenger:
    def __init__(self, id, name, money):
        self.id = id
        self.money = money
        self.name = name

    @staticmethod
    def is_valid_name(name):
        return len(name.split( )) >=2

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not self.is_valid_name(value):
            raise ValueError("Invalid name")
        else:
            self.__name = value

class Vehicle(ABC):
    def __init__(self, license_plate, amount_of_seats):
        self.license_plate = license_plate
        self.amount_of_seats = amount_of_seats
        self.__occupants = {}

    @property
    def occupants(self):
        return self.__occupants

    @property
    def number_of_occupants(self):
        return len(self.occupants)
    
    @property
    @abstractmethod
    def maximum_occupants():
        pass
        
    def add_passenger(self, passenger):
        if passenger.id in self.occupants:
            return
        elif self.number_of_occupants >= self.amount_of_seats:
            return
        else:
            self.occupants[passenger.id] = passenger

    def remove_passenger(self, passenger):
        if passenger.id in self.occupants:
            del self.occupants[passenger.id]

    def remove_all_passengers(self):
        self.occupants.clear()

    @property
    def occupant_names(self):
        return [passenger.name for passenger in self.occupants.values()]
    
class Taxi(Vehicle):
    def __init__(self, license_plate, amount_of_seats):
        super().__init__(license_plate, amount_of_seats)
        self.is_available = True

    @property
    def maximum_occupants(self):
        return self.amount_of_seats
    
    def pickup(self, passengers, distance):
        fare = max(5, 1 + distance)

        if not self.is_available or len(passengers) > self.maximum_occupants:
            raise ValueError("Taxi unavailable")

        if passengers[0].money < fare:
            raise RuntimeError("Not enough money")
        passengers[0].money -= fare
        [self.add_passenger(passenger) for passenger in passengers]
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
        if self.number_of_occupants >= self.maximum_occupants:
            raise RuntimeError("No seats available")
        elif passenger.money < 2:
            raise RuntimeError("Not enough money")
        else:
            passenger.money -= 2
            self.add_passenger(passenger)

    def disembark(self, passenger):
        self.remove_passenger(passenger)

passenger1 = Passenger("1654894", "Bob Bob", 15)
passenger2 = Passenger("31561561", "jhsfb jhdrdg", 20)
passenger3 = Passenger("31564561561", "jhsfb jdfnjhdrdg", 20)
taxi1 = Taxi("ABC 123", 4)
taxi1.pickup([passenger1, passenger2], 8)
print(taxi1.number_of_occupants)
taxi1.dropoff()
print(taxi1.number_of_occupants)
taxi1.pickup([passenger3], 8)
print(taxi1.number_of_occupants)
bus1 = Bus("ABC 123", 10)
bus1.board(passenger1)