from itertools import permutations, pairwise

def find_shortest_path(distance, city_count):
    def total_distance(path):
        return sum(distance(x, y) for x, y in pairwise(path))
    xd = ([0, *p, 0] for p in permutations(range(1, city_count)))
    return min(xd, key=total_distance)

# It makes sense as the key refers to the prior defined function.