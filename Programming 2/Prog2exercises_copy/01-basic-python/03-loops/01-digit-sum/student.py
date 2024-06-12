# Write your code here
def last_digit(n):
    return n % 10
print(last_digit(34))
def remove_last_digit(n):
    return n // 10
print(remove_last_digit(34))

def digit_sum(n):
    sum = last_digit(n)
    for digit in str(remove_last_digit(n)):
        sum += int(digit)
    return sum

print(digit_sum(34))