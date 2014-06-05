def sum_nth_power(n, number):
    return sum([int(i) ** n for i in str(number)])

def pr30(n):
    total = 0
    for i in range(2, 1000000):
        if sum_nth_power(n, i) == i:
            total += i
    return total

print pr30(5)


