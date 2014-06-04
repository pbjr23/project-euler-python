def list_product(l):
    """Returns the product of all of the numbers in the list"""
    output = 1
    for number in l:
        output *= number
    return output


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


def get_factors_2(n, with_original=True):
    """Outputs the factors of n as a list.
       Uses the prime factorization to generate all factors"""
    factorization = prime_factorization(n)
    all_factors = [1]
    init_powers = []
    prime_powers = {}

    for prime in factorization:
        powers = [prime ** i for i in range(1, factorization[prime] + 1)]
        all_factors.extend(powers)
        prime_powers[prime] = powers

    for i in range(2, len(prime_powers) + 1):
        combos = list_combinations(prime_powers.keys(), i)
        for combo in combos:
            powers = [prime_powers[i] for i in combo]
            all_factors.extend(product(powers))
    if with_original == True:
        return all_factors
    else:
        all_factors.remove(n)
        return all_factors


def get_factors(n):
    """Outputs the factors of n as a list"""
    if n == 1:
        return [1]
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if n / i == i:
                factors.append(i)
            else:
                factors.append(i)
                factors.append(n / i)
    return factors


def num_factors(n):
    """Returns number of factors of n, including n and 1"""
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if float(n) / i == float(i):
                count += 1
            else:
                count += 2
    return count


def product(iterables):
    """ Generates combinations of elements from each input list of list_lengths
        Takes multiple lists as input and returns all combinations using one 
        element from each list"""
    output = []
    num_iters = len(iterables)
    list_lengths = []
    list_remaining = [1]

    for i in xrange(num_iters - 1, -1, -1):
        m = len(iterables[i])
        list_lengths.insert(0, m)
        list_remaining.insert(0, m * list_remaining[0])
    nProducts = list_remaining.pop(0)

    for p in xrange(nProducts):
        current = []
        for i in xrange(num_iters):
            j = p / list_remaining[i] % list_lengths[i]
            current.append(iterables[i][j])
        output.append(list_product(current))
    return output


def list_combinations(l, n):
    """Generates combinations of size n from list l"""
    if n == 0:
        return [[]]
    else:
        return [[x] + suffix for i, x in enumerate(l)
                for suffix in list_combinations(l[i + 1:], n - 1)]


def factorial(n):
    """Returns factorial of number n"""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def nth_fibonacci_number(n, memo={0: 0, 1: 1}):
    """Prints the nth nth fibonacci number"""
    if not n in memo:
        memo[n] = nth_fibonacci_number(n - 1, memo) + \
            nth_fibonacci_number(n - 2, memo)
    return memo[n]


def alphabet_dictionary(reverse=False):
    """Returns a dictionary with letters as keys and numbers as values by default, reversed if reverse==True"""
    if reverse == True:
        return {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
    else:
        return {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}

        