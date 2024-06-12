def is_prime(n):
    return not any(n % i == 0 for i in range(2,n)) if n > 1 else False
# how do you read this lol

def primes():
    return (i for i in range(2, ) if is_prime(i))
# we leave the stop empty, as it's going to check further 
# along with each input if it's a prime number.