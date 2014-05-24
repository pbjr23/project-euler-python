one_nineteen = {0: 0,
                1: 3,
                2: 3,
                3: 5,
                4: 4,
                5: 4,
                6: 3,
                7: 5,
                8: 5,
                9: 4,
                10: 3,
                11: 6,
                12: 6,
                13: 8,
                14: 8,
                15: 7,
                16: 7,
                17: 9,
                18: 8,
                19: 8}

tens = {20: 6,
        30: 6,
        40: 5,
        50: 5,
        60: 5,
        70: 7,
        80: 6,
        90: 6}

def single_digit(n):
    global one_nineteen
    return one_nineteen[n]

def two_digit(n):
    global one_nineteen
    global tens
    if n < 20:
        return one_nineteen[n]
    return tens[(n / 10) * 10] + single_digit(n % 10)

def three_digit(n):
    # 'hundred and' is 10 letters
    # 'hundred' is 7 letters
    if n % 100 == 0:
        return 7 + single_digit(n / 100)
    else:
      return 10 + single_digit(n / 100) + two_digit(n % 100)

def number_word_length(n):
    if n < 10:
        return single_digit(n)
    if n < 100:
        return two_digit(n)
    if n < 1000:
        return three_digit(n)
    if n == 1000:
        return 11

def sum_of_digits_up_to(n):
    """Sum of digits from 1 to n, inclusive"""
    output = 0
    for i in range(1, n + 1):
        output += number_word_length(i)
    return output

print sum_of_digits_up_to(1000)

