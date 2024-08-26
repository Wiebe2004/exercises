class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        if 0 <= value <= 23:
            self.__hours = value
        else:
            raise ValueError("Uur moet tussen 0u en 23u zijn")

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        if 0 <= value <= 59:
            self.__minutes = value
        else:
            raise ValueError("Minuten moeten tussen 0min en 59min zijn")

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value):
        if 0 <= value <= 59:
            self.__seconds = value
        else:
            raise ValueError("Seconden moeten tussen 0s en 59s zijn")
