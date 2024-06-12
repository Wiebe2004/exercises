class CircularBuffer:
    def __init__(self, n):
        self.n = n
        self.arr = []

    def __len__(self):
        return len(self.arr)
    
    def __getitem__(self, index):
        return CircularBuffer(self.arr.index([index]))
    
    def add(self, item):
        if len(self.arr) < self.n:
            return CircularBuffer(self.arr.append(item))
        else:
            return CircularBuffer(self.arr.pop(0))