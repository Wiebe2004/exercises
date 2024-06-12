class Cycle:
    def __init__(self, item):
        self.item = iter(item)
        self.start = list(item)

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            return next(self.item)
        except StopIteration:
            self.item = iter(self.start)
            return next(self.item)