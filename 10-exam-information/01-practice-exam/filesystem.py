class StorageDevice:
    def __init__(self,block_size,block_count):
        self.__available_blocks = set(range(block_count)) #exclusive wilt zeggen zonder 0 vgm
        self.__used_blocks = set()
        self.__block_size = block_size

    @property
    def available_block_count(self):
        return self.__available_blocks
    
    @property
    def used_block_count(self):
        return self.__used_blocks
    
    @property
    def total_block_count(self):
        return self.__available_blocks + self.__used_blocks
    
    @property
    def block_size(self):
        return self.__block_size
    
