# enter your code here to solve the transporation assignment
# voer hier je code in om de vervoersvraag op te lossen

import re
from abc import ABC, abstractmethod
class Passenger:

    @staticmethod
    def is_valid_name(name):
        return re.fullmatch(r"(\w+\s+){1,}\w+", name)


    def __init__(self, id, name, money):
        if not self.is_valid_name(name):
            raise ValueError(f"invalid name: {name}")
        self.id = id
        self.money = money
        self.__name = name


    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if not self.is_valid_name(name):
            raise ValueError(f"invalid name: {name}")
        else:
            self.__name = name

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
    def maximum_occupants(self):
        pass
    
    def add_passenger(self, passenger):
        if passenger.id in self.occupants:
            return ValueError("passenger already exists")
        else:
            self.occupants[passenger.id] = passenger

    def remove_passenger(self, passenger):
        if passenger.id not in self.occupants:
            raise ValueError("Passenger does not exist")
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
            raise ValueError("taxi is not available")
        
        if passengers[0].money < fare:
            raise RuntimeError("not enough money")
        
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
            return RuntimeError("No more seat available")
        elif passenger.money < 2:
            return RuntimeError("not enough money")
        else:
            passenger.money -= 2
            self.add_passenger(passenger)
    
    def disembark(self, passenger):
        self.remove_passenger(passenger)

    



# enkele passagiers aanmaken
aimee = Passenger("12.34.56-789.01", "Fernand Aloïs Eufrasie Costermans", 40)
bastian = Passenger("01.02.03-040.05", "Bastian Li Backiel", 5)

# enkele voertuigen aanmaken
mijn_taxi = Taxi("1-NGL-760", 4)
mijn_bus = Bus("1-HUE-344", 30)


# samen een busrit maken; Bastian betaalt graag zelf
mijn_bus.board(aimee)
mijn_bus.board(bastian)

# de inwoners van de bus controleren
print(mijn_bus.occupant_names)


# ze stappen uit bij de dierentuin
mijn_bus.disembark(aimee)
mijn_bus.disembark(bastian)

# opnieuw de inwoners controleren
print(mijn_bus.occupant_names)


# Bastian wil voor het eerst alleen met de bus gaan en Aimee volgt hem in een taxi
# ze rijden slechts 5 km om zeker te zijn dat hij niet verdwaalt
mijn_bus.board(bastian)
mijn_taxi.pickup([aimee], 5)

# de inwoners in elk voertuig controleren
print(mijn_bus.occupant_names)

print(mijn_taxi.occupant_names)


# controleren hoeveel geld er nog over is in hun portemonnees
print(aimee.money)

print(bastian.money)
        
        
        