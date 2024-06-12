# Write your code here
def is_prime(n):
    for prime in range(2, n):
        if n % prime == 0:
            return False
    return n > 1