def sum_of_digits_of_power(n, p):
    expanded = str(n ** p)
    output = 0
    for digit in expanded:
        output += int(digit)
    return output

print sum_of_digits_of_power(2,1000)
