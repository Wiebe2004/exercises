def movie_count(movies, director):
    return len([movie for movie in movies if movie.director == director])


def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies if actor in movie.actors])


def is_prime(n):
    return all(n % k != 0 for k in range(2, n)) and n >= 2


def is_increasing(ns):
    return all(x <= y for x, y in zip(ns, ns[1:]))
