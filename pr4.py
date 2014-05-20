def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def pr4():
    all_palindromes = []
    for i in xrange(999, 99, -1):
        for j in xrange(i, 99, -1):
            if is_palindrome(i * j):
                all_palindromes.append(i * j)
    return max(all_palindromes)

print pr4()
