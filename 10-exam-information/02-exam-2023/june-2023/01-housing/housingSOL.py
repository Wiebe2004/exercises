# enter your code here to solve the housing assignment
# voer hier je code in om de huisvestingsvraag op te lossen
from abc import ABC, abstractmethod


class Person:
    @staticmethod
    def is_valid_name(name):
        return len(name.split()) >= 2

    def __init__(self, id, name, is_a_student):
        if not self.is_valid_name(name):
            raise ValueError("Name not valid!")
        self.id = id
        self.is_a_student = is_a_student
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not self.is_valid_name(name):
            raise ValueError("Name not valid")
        else:
            self.__name == name


class Residence(ABC):
    def __init__(self, address, area, number_of_rooms):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.__occupants = {}  # DICTIONARY!!

    @property
    def number_of_occupants(self):
        return len(self.__occupants)

    @property
    def maximum_occupants(self):
        min_area = self.area // 20  # max kamers 20vierkante meter per persoon
        min_rooms = self.number_of_rooms * 2  # aantal personen per kamer
        return min(
            min_area, min_rooms
        )  # We berekekn het maximum aantal kamers door het min te berekenen van de 2 waarden.

    def register_resident(self, person):
        if len(self.__occupants) >= self.maximum_occupants:
            raise ValueError("Niet genoeg plaats")
        else:
            if person.id not in self.__occupants:
                self.__occupants[person.id] = person

    def unregister_resident(self, id):
        del self.__occupants[id]

    @property
    def resident_names(self):
        return [person.name for person in self.__occupants.values()]

    @abstractmethod
    def calculate_value(self):
        ...


class Villa(Residence):
    def __init__(self, address, area, number_of_rooms, garage_capacity):
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity = garage_capacity

    def calculate_value(self):
        return (
            (25000 * self.number_of_rooms)
            + (2100 * self.area)
            + (10000 * self.garage_capacity)
        )


class StudentKot(Residence):
    def __init__(self, address, area):
        super().__init__(address, area, 1)

    def register_resident(self, person):
        if person.is_a_student:
            super().register_resident(person)
        else:
            raise RuntimeError("Not a student!")

    def calculate_value(self):
        return 150000 * (750 * self.area)

aimee = Person("12.34.56-789.01","Aimee Backiel",False)
bastian = Person("01.02.03-040.05", "Bastian Li Backiel", True)

# maak enkele woningen
my_villa = Villa("Roeselbergdal 44, 3012 Wilsele", 151, 4, 1)
my_kot = StudentKot("Kortestraat 6, 3000 Leuven",20)

# controleer de waarden van de eigenschappen
my_villa.calculate_value()

my_kot.calculate_value()

# Verhuis de mensen naar een woning
my_villa.register_resident(aimee)
my_villa.register_resident(bastian)

# controleer de bewoners van de villa
my_villa.resident_names

# Op een dag, helaas, zal Bastian opgroeien en verhuizen naar zijn studentenkot
my_villa.unregister_resident(bastian.id)
my_kot.register_resident(bastian)

# controleer de bewoners opnieuw
my_villa.resident_names

my_kot.resident_names

# Met al haar vrije tijd kan Aimee de garage uitbreiden om ruimte te maken voor al haar hobby's.
my_villa.garage_capacity = 3
my_villa.calculate_value()