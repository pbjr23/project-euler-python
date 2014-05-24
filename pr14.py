memo = {}

def collatz_length(n, count=1, init=0):
    global memo
    if count == 1:
        init = n
    if n in memo:
        value = count + memo[n] - 1
        memo[init] = value
        return value
    if n == 1:
        memo[init] = count
        return count
    elif n % 2 == 0:
        n = n / 2
    elif n % 2 == 1:
        n = 3*n + 1
    count += 1
    return collatz_length(n, count, init)

def pr14(n):
    global memo
    max = 0
    numb = 0
    for i in range(1, n):
        current = collatz_length(i)
        if current > max:
            max = current
            numb = i
    return numb

print pr14(1000000)
