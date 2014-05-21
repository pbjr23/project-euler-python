from mathtools import list_product


def parse_file(file):
    fin = open(file)
    l = [[int(i) for i in line.strip().split()] for line in fin]
    return l


def horizontal_max(l, adjacent):
    largest = 0
    for line in l:
        for i in xrange(len(line) - adjacent + 1):
            current = list_product(line[i:i + adjacent])
            if current > largest:
                largest = current
    return largest


def vertical_max(l, adjacent):
    largest = 0
    for column in xrange(len(l[0])):
        for row in xrange(len(l) - adjacent + 1):
            current = list_product([l[j][column]
                                   for j in range(row, row + adjacent)])
            if current > largest:
                largest = current
    return largest


def right_diagonal_max(l, adjacent):
    largest = 0
    for column in xrange(len(l[0]) - adjacent + 1):
        for row in xrange(len(l) - adjacent + 1):
            current = list_product([l[row + i][column + i]
                                   for i in range(adjacent)])
            if current > largest:
                largest = current
    return largest


def left_diagonal_max(l, adjacent):
    largest = 0
    for column in xrange(adjacent - 1, len(l[0])):
        for row in xrange(len(l) - adjacent + 1):
            current = list_product([l[row + i][column - i]
                                   for i in range(adjacent)])
            if current > largest:
                largest = current
    return largest


def all_max(l, adjacent):
    return max([horizontal_max(l, adjacent), vertical_max(l, adjacent), right_diagonal_max(l, adjacent), left_diagonal_max(l, adjacent)])

print all_max(parse_file('pr11.txt'), 4)
