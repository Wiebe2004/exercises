from itertools import pairwise

def total_distance(path, distance):
    xd = 0
    for x, y in pairwise(path):
        xd += distance(x, y)
    return xd


# there is a different possibility btw:
def total_distance2(path, distance):
    return sum(distance(x, y) for x, y in pairwise(path))