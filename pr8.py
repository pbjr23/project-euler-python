import mathtools

def largest_product(n):
    fin = open('pr8.txt')
    number = ''
    for line in fin:
        number += line.strip()
    l = [int(i) for i in list(str(number))]
    largest = 0
    for i in range(0, len(l) - n + 1):
        current_product = mathtools.list_product(l[i:i+n])
        if current_product > largest:
            largest = current_product
    return largest

print largest_product(13)
