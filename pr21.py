from mathtools import get_factors


def sum_proper_divisors(n):
    return sum(get_factors(n)) - n

def sum_amicable_numbers(n):
    output = 0
    for i in range(1, n):
        d = sum_proper_divisors(i)
        if sum_proper_divisors(d) == i and i != d:
            output += i
    return output

print sum_amicable_numbers(10000)