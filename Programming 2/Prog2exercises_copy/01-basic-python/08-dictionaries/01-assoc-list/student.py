class AssocList:
    def __init__(self):
        self.__items = []

    def __setitem__(self, key, value):
        for pair in self.__items:
            if pair[0] == key:
                pair[1] = value
                return
        self.__items.append([key, value])

    def __getitem__(self, key):
        for pair in self.__items:
            if pair[0] == key:
                return pair[1]
        raise KeyError()

    def __contains__(self, key):
        for pair in self.__items:
            if pair[0] == key:
                return True
        return False

    def __len__(self):
        return len(self.__items)

    @property
    def keys(self):
        return [pair[0] for pair in self.__items]

    @property
    def values(self):
        return [pair[1] for pair in self.__items]