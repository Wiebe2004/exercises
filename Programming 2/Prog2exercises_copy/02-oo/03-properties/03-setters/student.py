# Write your code here
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    @hours.setter
    def hours(self, value):
        if not 0 <= value < 24:
            raise ValueError('bro ain\'t right')
        self.__hours = value

    @minutes.setter
    def minutes(self, value):
        if not 0 <= value < 60:
            raise ValueError('bro ain\'t right')
        self.__minutes = value

    @seconds.setter
    def seconds(self, value):
        if not 0 <= value < 60: # if not is always an option
            raise ValueError('bro ain\'t right')
        self.__seconds = value