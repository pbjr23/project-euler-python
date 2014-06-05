def count(total, coins):
    # Total = 0 means we have found one way to make perfect change
    if total == 0:
        return 1
    # Doesn't add anything to the number of ways
    if total < 0 or len(coins) == 0:
        return 0
    # coins[1:] permutes for each type of coin
    else:
        return count(total, coins[1:]) + count(total - coins[0], coins)

print count(200, [1, 2, 5, 10, 20, 50, 100, 200])
