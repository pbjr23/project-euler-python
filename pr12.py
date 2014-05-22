import mathtools

def has_over_n_divisors(number, n):
    return mathtools.num_factors(number) > n

def triangular_with_over_n_divisors(n):
    triangular = 1
    incr = 2
    while not has_over_n_divisors(triangular, n):
        triangular += incr
        incr += 1
    return triangular

print triangular_with_over_n_divisors(500)