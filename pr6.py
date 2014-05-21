def sum_of_squares(n):
    output = 0
    for i in xrange(1, n + 1):
        output += i ** 2
    return output

def square_of_sum(n):
    output = 0
    for i in xrange(1, n + 1):
        output += i
    return output ** 2

print square_of_sum(100) - sum_of_squares(100)