# Write your code here
def is_increasing(ns):
    for i in range(len(ns)):
        for j in range(i+1, len(ns)):
            if ns[j] < ns[i]:
                return False
    return True