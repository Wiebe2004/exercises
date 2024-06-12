# enter your code here to solve the housing assignment
# voer hier je code in om de huisvestingsvraag op te lossen
from abc import abstractmethod, ABC
import re
import math



class Person:
    def __init__(self, id, name, is_a_student):
        if Person.is_valid_name(name):
            self.__name = name
        else:
            raise ValueError()
        self.id = id
        self.is_a_student = is_a_student

    @staticmethod
    def is_valid_name(name):
        if re.fullmatch(r'.+[ ].+([ ].+)*?', name):
            return True
        return False

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if Person.is_valid_name(name):
            self.__name = name
        else:
            raise ValueError()
        

        
class Residence(ABC):
    def __init__(self, address, area, number_of_rooms):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.__occupants = dict()


    @property
    def number_of_occupants(self):
        return len(self.__occupants)
    
    @property
    def maximum_occupants(self):
        p = self.area / 20
        k = self.number_of_rooms * 2
        return min(math.floor(p), k)
    
    def register_resident(self, person):
        if self.number_of_occupants < self.maximum_occupants:
            if person.id not in self.__occupants.keys():
                self.__occupants[person.id] = person.name
        elif self.number_of_occupants == self.maximum_occupants:
            raise RuntimeError()
        
    def unregister_resident(self, id):
        del self.__occupants[id]

    @property
    def resident_names(self):
        return list(self.__occupants.values())
    
    @abstractmethod
    def calculate_value(self):
        ...

            

class Villa(Residence):
    def __init__(self, address, area, number_of_rooms, garage_capacity):
        super().__init__(address=address, area=area, number_of_rooms=number_of_rooms)
        self.garage_capacity = garage_capacity

    def calculate_value(self):
        return ((25000 * self.number_of_rooms) + (2100 * self.area) + (10000 * self.garage_capacity))
    


class StudentKot(Residence):
    def __init__(self, address, area):
        super().__init__(address=address, area=area, number_of_rooms=1)

    def register_resident(self, person):
        if person.is_a_student:
            super().register_resident(person)
        else:
            raise RuntimeError()
    
    def calculate_value(self):
        return (150000 + (750 * self.area))
