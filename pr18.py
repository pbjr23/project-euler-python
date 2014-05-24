def maximum_path(file):
    data = []
    fin = open(file)
    for line in fin:
        data.append([int(i) for i in line.strip().split()])
    for line in range(1, len(data)):
        line_length = len(data[line])
        data[line][0] += data[line - 1][0]
        for element in range(1, line_length - 1):
            greater = max(data[line - 1][element], data[line - 1][element - 1])
            data[line][element] += greater
        data[line][line_length - 1] += data[line - 1][line_length - 2]
    return max(data[-1])

# print maximum_path('pr18.txt')
