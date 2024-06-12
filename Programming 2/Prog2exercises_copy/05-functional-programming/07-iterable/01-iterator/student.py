class InclusiveRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return InclusiveRangeIterator(self.start, self.end)

class InclusiveRangeIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            current = self.current
            self.current += 1
            return current