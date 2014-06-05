from math import log10

def largest_value(file):
    fin = open(file)
    largest = 0
    for line_number, line in enumerate(fin):
        numbers = line.strip().split(',')
        current = int(numbers[0]) ** log10(int(numbers[1]))
        print line_number, numbers, current
        if current > largest:
            largest = current
            largest_line = line_number + 1, numbers
    return largest_line

print largest_value(("pr99.txt"))

# 848 ['999665', '500894'] 27239.8248209
# 708 ['895447', '504922'] 26187.437115
