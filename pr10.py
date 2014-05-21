# import mathtools

# def sum_of_primes_under(n):
#     start = 3
#     total = 2
#     while start < n:
#         if mathtools.is_prime(start):
#             total += start
#         start += 2
#         if start < n and mathtools.is_prime(start):
#             total += start
#         start += 4
#     return total

# print sum_of_primes_under(2000000)

import math
prime_list = []
numb = 3

def prime_check(n):
    for i in xrange(2, int(math.sqrt(n)) + 1):
         if n % i == 0:
             return
    else:
        prime_list.append(n)

while numb < 2000000:
    prime_check(numb)
    numb += 2

print sum(prime_list)