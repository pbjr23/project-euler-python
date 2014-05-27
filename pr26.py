def cycle_length(n):
    """Returns the length of the cycle for the fraction 1 / n"""
    for power in xrange(1, n):
        if 10 ** power % n == 1:
            return power
    return 0

def generate_cycle_lengths(n):
    # The cycle length for n is cycle_lengths[n]
    cycle_lengths = [0]
    for i in xrange(1, n):
        cycle_lengths.append(cycle_length(i))
    return cycle_lengths

def max_cycle_length(n):
    lengths = generate_cycle_lengths(n)
    largest = 0
    number = 0
    for i in xrange(len(lengths)):
        if lengths[i] > largest:
            number = i
            largest = lengths[i]
    return number

print max_cycle_length(1000)
