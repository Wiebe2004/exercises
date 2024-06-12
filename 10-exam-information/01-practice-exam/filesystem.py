from abc import ABC, abstractmethod
import re


class StorageDevice:
    def __init__(self,block_size,block_count):
        self.__available_blocks = set(range(block_count)) #exclusive wilt zeggen zonder 0 vgm
        self.__used_blocks = set()
        self.__block_size = block_size

    @property
    def available_block_count(self):
        return len(self.__available_blocks)
    
    @property
    def used_block_count(self):
        return len(self.__used_blocks)
    
    @property
    def total_block_count(self):
        return len(self.__available_blocks) + len(self.__used_blocks) #Vergeet die len() nu is niet domme lul!
    
    @property
    def block_size(self):
        return self.__block_size
    
    def allocate(self, block_count):
        if block_count>self.__available_blocks:
            raise RuntimeError("No enough blocks")

        allocated_blocks = list(self.__available_blocks)[:block_count]

        for block in allocated_blocks:
            self.__available_blocks.remove(block)
            self.__used_blocks.add(block)
        return allocated_blocks
    
    def free(self,blocks):
        for block in blocks:
            if block not in self.__used_blocks:
                raise RuntimeError(block + " is not found in used blocks")
            else:
                self.__used_blocks.remove(block)
                self.__available_blocks.add(block)

class Entity(ABC):

    @staticmethod
    def is_valid_name(name):
        if re.fullmatch('^[A-Za-z0-9.]{1,16}', name):
            return True
        else:
            return False


    def __init__(self,storage,name):
        self.__storage = storage
        self.__name = name
        if not self.is_valid_name(name):
            raise RuntimeError("Name is not valid!")
            
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self,new_name):
        if not self.is_valid_name(new_name):
            raise RuntimeError("Name is nog valid")
        else:
            self.__name = new_name
    
    @property
    def storage(self):
        return self.__storage

    @property
    @abstractmethod
    def size_in_blocks(self):
        pass

    @property
    def size_in_bytes(self):
        return self.size_in_blocks*self.storage.block_size
    
    @abstractmethod
    def clear(self):
        pass

class File(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.__blocks = set()

    def grow(self,block_count):
        self.__blocks.update(self.storage.allocate(block_count))  
        #Definieer een alleen-lezen eigenschap size_in_blocks die het aantal blokken teruggeeft dat wordt bezet door het Bestand.
        #Met de functie allocatie in StorageDevice(storage) voeg je blokken toe

    @property
    def size_in_blocks(self):
        return len(self.__blocks)

    def clear(self):
        self.storage.free(self.__blocks)
        self.__blocks = set()

                
class Directory(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.children = [] #EMPTY LIST

    def add(self,entity):
        self.children.append(entity)

    @property
    def size_in_blocks(self):
        return sum([child.size_in_blocks for child in self.children])
    
    def clear(self):
        [child.clear() for child in self.children]
        # self.children.clear()
