def is_prime(n):
    """Returns true if a number is prime, false if not"""
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for i in xrange(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    """Outputs a list of primes up to and including n"""
    output = []
    if n <= 1:
        return output
    if n <= 2:
        return [2]
    for i in xrange(3, n + 1, 2):
        if is_prime(i):
            output.append(i)
    return output

print generate_primes(10)