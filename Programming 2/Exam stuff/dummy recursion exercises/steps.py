def walk(steps):
    if steps == 0:
        return
    walk(steps - 1) # The position of the recursion also depends on when or whenever you want to print it.
    print(f'You take step #{steps}')
    #walk(steps - 1)
walk(5)