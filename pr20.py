from mathtools import factorial


def factorial_digit_sum(n):
    numb = factorial(n)
    return sum([int(i) for i in str(numb)])


print factorial_digit_sum(100)
