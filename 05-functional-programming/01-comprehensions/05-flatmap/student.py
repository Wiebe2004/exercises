from util import Card
import movie as movies

def genres(movies):
    return {
        genre 
        for movie in movies
        for genre in movie.genres 
    }

def actors(movies):
    return {
        actor
        for movie in movies
        for actor in movie.actors
    }

def repeat_consecutive(xs, n):
    return [
        x 
        for x in xs
        for _ in range(n)
    ]

def repeat_alternating(xs, n):
    return [
        x
        for _ in range(n) #Buitenste lus, deze word n keer gedaan.
        for x in xs #Elke keer als de buitenste lus gedaan word word deze lus herhaald. 
    ]

def cards(values, suits):
    return{
        Card(value,suit)
        for value in values
        for suit in suits
    }
# print(actors(movies.movies))
print(cards([2, 5, 10], ['hearts', 'diamonds']))