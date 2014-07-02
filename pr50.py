from mathtools import generate_primes, is_prime

all_primes = generate_primes(1000000)

def n_consecutive_sum(n, all_primes):
    largest_sum = 0
    bob = []
    for i in range(len(all_primes) - n):
        current = sum(all_primes[i:i+n])
        if current > largest_sum and is_prime(current):
            largest_sum = current
            bob = all_primes[i:i+n]
    return largest_sum, bob


def longest_consecutive_sum(limit):
    all_primes = generate_primes((limit + 1) / 2)
    for i in range(len(all_primes) - n):
        current = sum(all_primes[i:i+n])
        if current > largest_sum and is_prime(current):
            largest_sum = current
            bob = all_primes[i:i+n]
    return largest_sum, bob


# print n_consecutive_sum(21, all_primes)

# for i in range(len(all_primes)):
#     for j in range(i+1, len(all_primes)):
        
# for start in range(len(all_primes)):
#     temp_sum = all_primes[start]
#     for end in range(start + 1, len(all_primes)):
#         temp_sum += all_primes[end]
#         if not is_prime(temp_sum):
#             temp_sum -= all_primes[end]
#             break
#     print all_primes[start], temp_sum
