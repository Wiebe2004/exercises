# enter your code here to solve the housing assignment
# voer hier je code in om de huisvestingsvraag op te lossen
import re
from abc import ABC, abstractmethod

class Person:
    @staticmethod
    def is_valid_name(name):
        return re.fullmatch(r"\w+\s\w+(\s\w+)*", name)
    
    def __init__(self, id, name, is_a_student):
        self.id = id
        self.name = name
        self.is_a_student = is_a_student
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not Person.is_valid_name(value):
            raise ValueError
        self.__name = value
        
class Residence(ABC):
    def __init__(self, address, area, number_of_rooms):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.__occupants = {}
        
    @property
    def number_of_occupants(self):
        return len(self.__occupants)
    
    @property
    def maximum_occupants(self):
        min_area = self.area // 20
        min_rooms = self.number_of_rooms * 2
        
        return min(min_area, min_rooms)
    
    @property
    def resident_names(self):
        return [person.name for person in self.__occupants.values()]
            
    def register_resident(self, person):
        if person.id in self.__occupants.keys():
            pass
        elif self.number_of_occupants == self.maximum_occupants:
            raise RuntimeError
        self.__occupants[person.id] = person
        
    def unregister_resident(self, id):
        if id in self.__occupants.keys():
            self.__occupants.pop(id)
            
    @abstractmethod
    def calculate_value(self):
        ... 
        
class Villa(Residence):
    def __init__(self, address, area, number_of_rooms, garage_capacity):
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity = garage_capacity
        
    def calculate_value(self):
        return (25000 * self.number_of_rooms) + (2100 * self.area) + (10000 * self.garage_capacity)
        

class StudentKot(Residence):
    def __init__(self, address, area):
        super().__init__(address, area, 1)
    
    def calculate_value(self):
        return 150000 + (750 * self.area)
    
    def register_resident(self, person):
        if not person.is_a_student:
            raise RuntimeError
        super().register_resident(person)
        
aimee = Person("12.34.56-789.01","Aimee Backiel",False)
bastian = Person("01.02.03-040.05", "Bastian Li Backiel", True)

my_villa = Villa("Roeselbergdal 44, 3012 Wilsele", 151, 4, 1)
my_kot = StudentKot("Kortestraat 6, 3000 Leuven",20)

print(my_villa.calculate_value())

print(my_kot.calculate_value())

my_villa.register_resident(aimee)
my_villa.register_resident(bastian)

print(my_villa.resident_names)

my_villa.unregister_resident(bastian.id)
my_kot.register_resident(bastian)

print(my_villa.resident_names)

print(my_kot.resident_names)

my_villa.garage_capacity = 3
print(my_villa.calculate_value())