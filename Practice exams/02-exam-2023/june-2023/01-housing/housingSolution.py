# enter your code here to solve the housing assignment
# voer hier je code in om de huisvestingsvraag op te lossen
from abc import ABC, abstractmethod

class Person:
    def __init__(self, id, name, is_a_student):
        self.id = id
        self.is_a_student = is_a_student
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
            raise ValueError("invalid name")
        else:
            self.__name = value

class Residence(ABC):
    def __init__(self, address, area, number_of_rooms):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.__occupants = {}

    @property
    def number_of_occupants(self):
        return len(self.number_of_occupants)
    
    @property
    def maximum_occupants(self):
        mppa = self.area // 20
        mppr = self.number_of_rooms * 2
        return min(mppa, mppr)
    
    def register_resident(self, person):
        if person.id in self.__occupants:
            return
        elif self.maximum_occupants <= self.number_of_occupants:
            raise RuntimeError("residence full")
        else:
            self.__occupants[person.id] = person
    
    def unregister_resident(self, person):
        if person.id in self.__occupants:
            del self.__occupants[person.id]

    @property 
    def resident_name(self):
        return [person.name for person in self.__occupants.values()] 
     
    @abstractmethod
    def calculate_value():
        pass

class Villa(Residence):
    def __init__(self, address, area, number_of_rooms, garage_capacity):
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity = garage_capacity

    def calculate_value(self):
        return (25000 * self.number_of_rooms) + (2100 * self.area) + (10000 * self.garage_capacity)

class StudentKot(Residence):
    def __init__(self, address, area):
        super().__init__(address, area, 1)

    def register_resident(self, person):
        if person.is_a_student:
            super().register_resident(person)
        else:
            raise RuntimeError("not a student")
        
    def calculate_value(self):
        return 150000 + (750 * self.area)