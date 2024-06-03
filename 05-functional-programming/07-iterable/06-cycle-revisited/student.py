def cycle(xs):
    values = list(xs)
    while True:
        for value in values:
            yield value
            

#From solution 
# def alternative_cycle(values):
#     values = list(values)
#     while True:
#         yield from values  # "yield from xs" yields each element in xs in turn
