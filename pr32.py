def is_pandigital(multiplicand, multiplier):
    pandigital_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    product = multiplier * multiplicand
    all_digits = "%s%s%s" % (multiplicand, multiplier, product)
    all_digits = [int(digit) for digit in all_digits]
    all_digits.sort()
    return all_digits == pandigital_digits

def pr32():
    output = []
    for i in xrange(1, 100):
        for j in xrange(100, 1000):
            if is_pandigital(i, j):
                output.append(i*j)
    for i in xrange(1, 10):
        for j in xrange(1000, 10000):
            if is_pandigital(i, j):
                output.append(i*j)
    return sum(set(output))

print pr32()

