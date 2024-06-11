# Write your code here
def rotate(xs, n):
    n = n % len(xs)
    left = xs[:n]
    right = xs[n:]
