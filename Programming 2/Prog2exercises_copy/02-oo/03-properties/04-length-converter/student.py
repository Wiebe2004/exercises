class LengthConverter:
    def __init__(self):
        self.__meter = 0
        self.__feet = 0
        self.__inch = 0

    @property
    def meter(self):
        return self.__meter
    
    @property
    def feet(self):
        return self.__feet
    
    @property
    def inch(self):
        return self.__inch
    
    @meter.setter
    def meter(self, value):
        self.__meter = value
        self.__feet = value * 3.281
        self.__inch = value * 39.37

    @feet.setter
    def feet(self, value):
        self.__feet = value
        self.__meter = value / 3.281
        self.__inch = value * 12


    @inch.setter
    def inch(self, value):
        self.__inch = value
        self.__feet = value / 12
        self.__meter = value / 39.37