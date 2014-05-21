import mathtools

def sum_of_primes_under(n):
    start = 2
    total = 0
    while start < n:
        total += start
        start = mathtools.get_next_prime(start)
    return total

print sum_of_primes_under(2000000)

