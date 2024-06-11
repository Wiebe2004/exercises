# Write your code here

#long version
def median(ns):
    sorted_list = sorted(ns)
    print(sorted_list)
    length = len(sorted_list)
    if length%2 != 0:
        index = length // 2
        return sorted_list[index]
    else:
        left = (length // 2) - 1
        right = length // 2
        median = (sorted_list[left]+sorted_list[right]) / 2
        return median


def median_short(ns):
    sorted_list = sorted(ns)
    length = len(sorted_list)
    i = length // 2
    if length%2 != 0:
        return sorted_list[i]
    else:
       return (sorted_list[i-1]+sorted_list[i]) / 2
    
print(median_short([4, 2, 6, 5, 4, 1, 2, 7, 6, 4, 5, 9]))