import mathtools

def largest_prime_factor(n):
    factorization = mathtools.prime_factorization(n)
    return max(factorization.keys())


print largest_prime_factor(600851475143)
