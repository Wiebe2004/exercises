# Write your code here
def rotate(xs, n):
    temp = xs[:n]
    xs[:] = xs[n:]
    xs.extend(temp)