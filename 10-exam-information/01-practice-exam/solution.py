# Enter your code here:
# from abc import abstractmethod
from abc import ABC, abstractmethod
import re


class StorageDevice:
    def __init__(self, block_count, block_size):
        self.__block_size = block_size
        self.__available_blocks = set(range(block_count))
        self.__used_blocks = set()

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
        if block_count > self.__available_blocks:
            raise RuntimeError("No sufficient blocks")

        allocated_blocks = list(self.__available_blocks)[:block_count] #Deze regel allocated_blocks = list(self.__available_blocks)[:block_count] maakt een nieuwe lijst genaamd allocated_blocks. Deze lijst bevat de eerste block_count elementen van de set self.__available_blocks.

        for block in allocated_blocks:
            self.__available_blocks.remove(block)
            self.__used_blocks.add(block)
        return allocated_blocks

    def free(self, blocks):
        for block in blocks:
            if block not in self.__used_blocks:
                raise RuntimeError()
            else:
                self.__available_blocks.add(block)
                self.__used_blocks.remove(block)





class Entity(ABC):
    @staticmethod
    def is_valid_name(name):
        if 0 <= len(name) < 16 and re.fullmatch(r"^[A-Za-z0-9.]+$", name):
            return True
        else:
            return False
    
    def __init__(self, storage, name):
        if not self.is_valid_name(name):
            raise RuntimeError()
        self.__storage = storage
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not self.is_valid_name(new_name):
            raise RuntimeError()
        self.__name = new_name

    @property
    def storage(self):
        return self.__storage

    @property
    def size_in_bytes(self):
        return self.size_in_blocks * self.storage.block_size

    @property
    @abstractmethod
    def size_in_blocks(self):
        pass

    @abstractmethod
    def clear(self):
        pass

class File(Entity):
    def __init__(self,storage,name):
        super().__init__(storage,name)
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
    
    def add(self,entity):
        self.children.append(entity)

    @property
    def size_in_blocks(self):
        return sum([child.size_in_blocks for child in self.children])
    
    def clear(self):
        [child.clear() for child in self.children]
        # self.children.clear()