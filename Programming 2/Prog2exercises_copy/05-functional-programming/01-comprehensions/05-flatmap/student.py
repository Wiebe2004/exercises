from util import Card

def genres(movies):
    return {genre for m in movies for genre in m.genres}


def actors(movies):
    return {actor for m in movies for actor in m.actors}


def repeat_consecutive(xs, n):
    return sorted([ys for ys in xs]*n)


def repeat_alternating(xs, n):
    return [ys for ys in xs]*n


def cards(values, suits):
    return {Card(value, suit) for value in values for suit in suits}
    # An object uses syntax like this "Card(item)" or "Card(item1, item2)"