import mathtools

print 600851475143

def largest_prime_factor(n):
    start = n
    while n % 2 != 0 and not mathtools.is_prime(n):
        n -= 1
    return n


print largest_prime_factor(600851475143)