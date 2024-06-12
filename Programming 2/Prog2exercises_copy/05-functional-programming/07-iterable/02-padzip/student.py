class PadZip:
    def __init__(self, left, right, padding=None):
        self.left = iter(left)
        self.right = iter(right)
        self.padding = padding

    def __iter__(self):
        return self

    def __next__(self):
        left = self.padding
        right = self.padding
        try:
            left = next(self.left)
        except StopIteration:
            pass

        try:
            right = next(self.right)
        except StopIteration:
            pass

        
        if left is self.padding and right is self.padding:
            raise StopIteration
        else:
            return (left, right)