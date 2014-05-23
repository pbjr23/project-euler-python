def first_n_digits_of_sum(file, n):
    fin = open(file)
    total = 0
    for i in fin:
        total += int(i.strip())
    return str(total)[:n]

print first_n_digits_of_sum('pr13.txt', 10)