from datetime import date


class Calendar:
    def __init__(self):
        self.__today = date.today()

    @property
    def today(self):
        return self.__today


class CalendarStub:
    def __init__(self, today):
        self.__today = today

    @property
    def today(self):
        return self.__today

    @today.setter
    def today(self, date):
        self.__today = date

cal = CalendarStub(date(2021, 12, 12))
print(cal.today)
cal.today = date(2012, 12, 12)
print(cal.today)