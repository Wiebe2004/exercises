import re

def movie_count(movies, director):
    return len([m.director for m in movies if director == m.director])


def longest_movie_runtime_with_actor(movies, actor):
    return max([m.runtime for m in movies if actor in m.actors])


def has_director_made_genre(movies, director, genre):
    return any([m.genres for m in movies if director in m.director if genre in m.genres])


def is_prime(n):
    if n <= 1:
        return False
    return not any(n % i == 0 for i in range(2, n))
    # I thought I had to make everything in a one-liner... which caused me to try all kinds of things lol


def is_increasing(ns):
    return all(ns[i] <= ns[i+1] for i in range(len(ns) - 1))
    # Checks the ns[i+1] if it's increasing, it also counts the iteration that equals to ns[i].
    # Goes in a for loop all the way to the end of the list.


def count_matching(xs, ys):
    # The first approach is more efficient as it avoids the making of a list.
    return sum(1 for i, j in zip(xs, ys) if i == j)
    # initial solution with the list & len() approach:
    return len([i for i, j in zip(xs, ys) if i == j])


def weighted_sum(ns, weights):
    return sum(i * j for i, j in zip(ns, weights))
    # zip has a specific syntax to respect here


def alternating_caps(string):
    return ''.join((a.upper() if i % 2 == 0 else a.lower() for i, a in enumerate(string)))
    # The enumerate function in Python returns an iterable that produces tuples of the form (index, element). 
    # So when you write for i, a in enumerate(string), i is the index of the element a in the string.


def find_repeated_words(sentence):
    words = re.split(r'\W+', sentence.lower())
    return {words[i] for i in range(len(words) - 1) if words[i] == words[i + 1]}
    # the usage of regex simplifies the filtering of the string.