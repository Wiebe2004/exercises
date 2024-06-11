from abc import ABC, abstractmethod
import re
class StorageDevice:

    def __init__(self, block_count, block_size):
        self.__available_blocks = set(range(block_count))
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
        return self.used_block_count + self.available_block_count
    
    @property
    def block_size(self):
        return self.__block_size
    
    def allocate(self, block_count):
        if block_count > self.available_block_count:
            raise RuntimeError("Not enough blocks available")
        blocks = list(self.__available_blocks)[:block_count]
        self.__available_blocks.difference_update(blocks)
        self.__used_blocks.update(blocks)
        return blocks
    
    def free(self, blocks):
        if not set(blocks).issubset(self.__used_blocks):
            raise RuntimeError("Blocks to free are not currently used")

        self.__available_blocks.update(set(blocks)) 
        self.__used_blocks.difference_update(set(blocks))

class Entity(ABC):
    def __init__(self, storage, name):
        self.name = name
        self.__storage = storage

    @staticmethod
    def is_valid_name(name):
        if re.fullmatch("[a-z|A-Z|0-9|.]*", name):
            if 0 < len(name) < 17:
                return True
        return False
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if self.is_valid_name(value):
            self.__name = value
        else:
            raise RuntimeError("Invalid name")
        
    @property
    def storage(self):
        return self.__storage
    
    @property
    @abstractmethod
    def size_in_blocks(self):
        pass

    @property
    def size_in_bytes(self):
        return self.size_in_blocks * self.storage.block_size
    
    @abstractmethod
    def clear(self):
        pass

class File(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.__blocks = set()
    
    def grow(self, block_count):
        self.__blocks.update(self.storage.allocate(block_count))
    
    def clear(self):
        self.storage.free(self.__blocks)
        self.__blocks = set()
    
    @property
    def size_in_blocks(self):
        return len(self.__blocks)
    
class Directory(Entity):

    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.children = []

    def add(self, entity):
        self.children.append(entity)

    @property
    def size_in_blocks(self):
        return sum([child.size_in_blocks for child in self.children])
    
    def clear(self):
        [child.clear() for child in self.children]