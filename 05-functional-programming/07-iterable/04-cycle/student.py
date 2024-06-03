# class Cycle:
#     def __init__(self, elts):
#         self.__elts = list(elts)
#         self.__index = -1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         self.__index = self.__elts
#         return self.__elts

class Cycle:
    def __init__(self, elts):
        self.__elts = list(elts)   # Converteer elts naar een lijst en sla op in self.__elts
        self.__index = -1          # Initialisatie van de index naar -1

    def __iter__(self):
        return self  # Retourneert het huidige object zelf als de iterator

    def __next__(self):
        # Verhoog de index en zorg ervoor dat het binnen de grenzen van de lijst blijft
        self.__index = (self.__index + 1) % len(self.__elts)
        # Retourneer het element op de huidige index
        return self.__elts[self.__index]
