def sum_diagonals_spiral(n):
    if n % 2 != 1:
        return False
    return (4 * n ** 3 + 3 * n ** 2 + 8 * n - 9) / 6 

print sum_diagonals_spiral(1001)