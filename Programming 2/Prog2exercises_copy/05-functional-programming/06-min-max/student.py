from math import sqrt

def closest(points, target_point):
    close = min(points, key=lambda point : sqrt((point[0] - target_point[0]) ** 2 + (point[1] - target_point[1]) ** 2))
    return close
# my bad, throwback to the fundamentals lol. This implements the maths aka square root.