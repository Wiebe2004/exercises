class PadZip:
    def __init__(self, left, right, padding=None):
        self.__left = iter(left)
        self.__right = iter(right)
        self.__padding = padding

    def __iter__(self):
        return self

    def __next__(self):
        left = next(self.__left, self.__padding)
        right = next(self.__right, self.__padding)

        if left is self.__padding and right is self.__padding:
            raise StopIteration()

        return (left, right)
