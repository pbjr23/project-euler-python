from mathtools import is_prime


def num_consecutive_primes(a, b):
    n = 0
    while is_prime(n ** 2 + a * n + b):
        n += 1
    return n

def pr27(a, b):
    max_primes = 0
    for i in range(-a, a + 1):
        for j in range(-b, b + 1):
            num_primes = num_consecutive_primes(i, j) 
            if num_primes > max_primes:
                max_primes = num_primes
                c = i * j
    return c


print pr27(1000, 1000)
