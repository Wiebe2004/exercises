# Write your code here
def remove_duplicates(xs):
    seen = set()
    ys = []

    for i in xs:
        if i not in seen:
            ys.append(i)
            seen.add(i)
    return ys