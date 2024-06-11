# Write your code here
def contains_duplicates(xs):
    k = []
    for j in range(len(xs)):
        if xs[j] in k:
            return True
        else:
            k.append(xs[j])
    return False


print(contains_duplicates([3, 5, 6, 7]))


# solution
def contains_duplicates_solution(xs):
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] == xs[j]:
                return True

    return False
