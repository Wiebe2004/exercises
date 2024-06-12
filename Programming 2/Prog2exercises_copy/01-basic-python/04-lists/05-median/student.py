# Write your code here
def median(ns):
    sortedlst = sorted(ns)
    index = (len(ns) - 1) // 2

    if (len(ns) % 2):
        return sortedlst[index]
    else:
        return (sortedlst[index] + sortedlst[index + 1])/ 2