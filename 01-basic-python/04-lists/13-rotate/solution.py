def rotate(xs, n):
    for _ in range(n):
        x = xs.pop(0)
        xs.append(x)

    return xs

print(rotate([1, 2, 3, 4, 5], 2))