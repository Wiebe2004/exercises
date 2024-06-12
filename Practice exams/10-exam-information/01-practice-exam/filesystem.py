import re
from abc import ABC, abstractmethod

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
        return len(self.__available_blocks) + len(self.__used_blocks)
    
    @property
    def block_size(self):
        return self.__block_size
    
    def allocate(self, block_count):
        if block_count > len(self.__available_blocks):
            raise RuntimeError()
        
        allocated_blocks = []
        for _ in range(block_count):
            block = self.__available_blocks.pop()
            self.__used_blocks.add(block)
            allocated_blocks.append(block)
        return allocated_blocks
            
    def free(self, blocks):
        if not all(block in self.__used_blocks for block in blocks):
            raise RuntimeError
        for block in blocks:
            self.__available_blocks.add(block)
            self.__used_blocks.remove(block)

class Entity(ABC):
    @staticmethod
    def is_valid_name(name):
        return re.fullmatch("^[A-Za-z0-9.]{1,16}$", name)
    
    def __init__(self, storage, name):
        if not self.is_valid_name(name):
            raise RuntimeError
        self.__name = name
        self.__storage = storage
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if not self.is_valid_name(new_name):
            raise RuntimeError
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
        return self.size_in_blocks * self.__storage.block_size
    
    @abstractmethod
    def clear(self):
        pass
        
class File(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.used_blocks = set()
        
    def grow(self, block_count):
        allocated = self.storage.allocate(block_count)
        self.used_blocks.update(allocated)
        
    @property
    def size_in_blocks(self):
        return len(self.used_blocks)
    
    def clear(self):
        self.storage.free(list(self.used_blocks))
        self.used_blocks.clear()

        
class Directory(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.children = []
    
    def add(self, entity):
        self.children.append(entity)
        
    @property
    def size_in_blocks(self):
        return self.storage.used_block_count
    
    def clear(self):
        for child in self.children:
            child.clear()
        self.children = []
            
# my_ssd = StorageDevice(1000, 4096)
# directory = Directory(my_ssd, 'myfolder')

# print(directory.size_in_blocks)

# file1 = File(my_ssd, 'file1')
# file1.grow(5)
# directory.add(file1)

# print(directory.size_in_blocks)

# file2 = File(my_ssd, 'file2')
# file2.grow(10)

# directory.add(file2)
# print(directory.size_in_blocks)

# subdir = Directory(my_ssd, 'subdir')
# directory.add(subdir)
# file3 = File(my_ssd, 'file3')
# file3.grow(20)
# subdir.add(file3)

# print(directory.size_in_blocks)
# directory.clear()
# print(directory.size_in_blocks)
# print(file1.size_in_blocks)
# print(file2.size_in_blocks)
# print(file3.size_in_blocks)