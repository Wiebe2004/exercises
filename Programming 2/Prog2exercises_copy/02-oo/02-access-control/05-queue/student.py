class Queue:
    def __init__(self):
        self.__queue = []

    def add(self, item):
        self.__queue.append(item)

    def next(self):
        if self.__queue:
            return self.__queue.pop(0)
        else:
            return None
    
    def is_empty(self):
        return len(self.__queue) == 0