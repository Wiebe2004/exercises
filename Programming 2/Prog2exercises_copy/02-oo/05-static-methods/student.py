class Duration:
    def __init__(self, seconds):
        self.seconds = seconds

    @property
    def seconds(self):
        return self.__seconds
    
    @property
    def minutes(self):
        return self.__seconds / 60
    
    @property
    def hours(self):
        return self.__seconds / 3600
    
    @seconds.setter
    def seconds(self, value):
        if value < 0:
            raise ValueError("no negatives")
        self.__seconds = value
    
    @staticmethod
    def from_seconds(seconds):
        return Duration(seconds)
    
    @staticmethod
    def from_minutes(minutes):
        return Duration(minutes * 60)

    @staticmethod
    def from_hours(hours):
        return Duration(hours * 3600)
    
# Here you have to keep in mind with the assignment explanation.
# static method basically means that the method isn't being in use in the constructor!!
# you have to make the read-only properties + static methods, proceed calling them out with the class.