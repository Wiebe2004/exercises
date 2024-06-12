class Repeat:
    def __init__(self, item):
        self.item = item

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.item
    

# nothing complex, just repeats upon itself.