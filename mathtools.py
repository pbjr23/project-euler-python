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
    output = [2]
    if n <= 1:
        return []
    if n <= 2:
        return output
    for i in xrange(3, n + 1, 2):
        if is_prime(i):
            output.append(i)
    return output


def get_next_prime(n):
    """Gets the next prime number after n"""
    if n < 2:
        return 2
    if n % 2 == 0:
        if is_prime(n + 1):
            return n + 1
        n += 1
    while not is_prime(n + 2):
        n += 2
    return n + 2


def get_previous_prime(n):
    """Gets the previous prime number before n"""
    if n == 2:
        return
    while not is_prime(n - 1):
        n -= 1
    return n - 1


def get_previous_divisible_prime(n, p):
    """Gets the previous prime number before p that is divisible by n"""
    p = get_previous_prime(p)
    while n % p != 0:
        p = get_previous_prime(p)
        if p == 2:
            return
    return p


def get_next_divisible_prime(n, p):
    """Gets the next prime number after p that is divisible by n"""
    p = get_next_prime(p)
    while n % p != 0:
        p = get_next_prime(p)
        if p > n:
            return
    return p


def prime_factorization(n):
    """Outputs the prime factorization of a number, in dictionary form"""
    if n == 1:
        return {1: 1}
    output = {}
    prime = get_next_divisible_prime(n, 0)
    while n != 1:
        while n % prime == 0:
            if prime not in output:
                output[prime] = 1
            else:
                output[prime] += 1
            n = n / prime
        prime = get_next_divisible_prime(n, prime)
    return output


def factorized_to_number(n):
    """Turns the dictionary factorization into a number"""
    output = 1
    for prime in n:
        output *= prime ** n[prime]
    return output


def list_product(l):
    """Returns the product of all of the numbers in the list"""
    output = 1
    for number in l:
        output *= number
    return output
