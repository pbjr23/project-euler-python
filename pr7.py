import mathtools

def nth_prime(n):
    start = 0
    for i in range(n):
        prime = mathtools.get_next_prime(start)
        start = prime
    return prime

print nth_prime(10001)