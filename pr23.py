from mathtools import get_factors

def is_abundant(n):
    """Returns if a number is abundant or not"""
    raw_sum = sum(get_factors(n))
    return raw_sum - n > n

def get_abundant_numbers(n):
    """Generates all abundant numbers less than n"""
    abundant = []
    for i in range(1, n):
        if is_abundant(i):
            abundant.append(i)
    return abundant

def get_abundant_sums(n):
    """Returns a list of all of the possible sums of two abundant numbers less than n"""
    all_numbers = []
    abundant = get_abundant_numbers(n)
    count = len(abundant)
    for i in xrange(count):
        for j in xrange(i, count):
            total = abundant[i] + abundant[j] 
            if total < n:
                all_numbers.append(total)
    return all_numbers

def filter(sums, n):
    """Filters out the elements in sums from the numbers [1, 2,...,n - 1]"""
    all_numbers = [i for i in range(1, n)]
    for element in sums:
        all_numbers[element - 1] = None
    return [i for i in all_numbers if i != None]

def pr23(n):
    all_sums = get_abundant_sums(n)           
    return sum(filter(all_sums, n))

print pr23(28124)