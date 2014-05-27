from mathtools import nth_fibonacci_number

def number_of_digits(n):
    i = 1
    while (len(str(nth_fibonacci_number(i))) < n):
        i += 1
    return i

print number_of_digits(1000) 