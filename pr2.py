def fib_sum_under(n):
    """Returns the sum of all of the even fibonacci numbers under n"""
    fib_sum = 0
    first = 1
    second = 1
    while second < n:
        if second % 2 == 0:
            fib_sum += second
        second_copy = second
        second = first + second
        first = second_copy
    return fib_sum

print fib_sum_under(4000000)
