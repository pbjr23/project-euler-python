import mathtools


def divisible_by(n):
    output = {}
    for i in xrange(1, n + 1):
        factorized = mathtools.prime_factorization(i)
        for number in factorized:
            if number not in output:
                output[number] = factorized[number]
            if number in output and factorized[number] > output[number]:
                output[number] = factorized[number]
    return mathtools.factorized_to_number(output)

print divisible_by(20)
