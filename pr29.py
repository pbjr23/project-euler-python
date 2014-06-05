def pr29(a, b):
    distinct = []
    for i in range(2, a + 1):
        for j in range(2, b + 1):
            value = i ** j
            if value not in distinct:
                distinct.append(value)
    return len(distinct)

print pr29(100, 100)
