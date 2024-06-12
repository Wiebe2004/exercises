def fizzbuzz():
    i = 1
    while True:
        if i % 3 == 0 and i % 5 == 0:
            yield 'fizzbuzz'
        elif i % 3 == 0:
            yield 'fizz'
        elif i % 5 == 0:
            yield 'buzz'
        else:
            yield str(i)
        i += 1

# it takes no parameter, so you to improvise it with a variable "i" for the index.
