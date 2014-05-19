def is_bouncy(n):
    arr = []
    for number in str(n):
        arr.append(int(number))
    if all(arr[i+1] >= arr[i] for i in range(len(arr) - 1)):
        return False
    if all(arr[i+1] <= arr[i] for i in range(len(arr) - 1)):
        return False
    return True

# def percent_bouncy(n):
#     bouncy = 0
#     for i in range(1, n+1):
#         if is_bouncy(i):
#             bouncy += 1
#     return float(bouncy)/n

# def binary_search(low, high):
#     midpoint = (low + high) / 2
#     print midpoint, percent_bouncy(midpoint)
#     if percent_bouncy(midpoint) < 0.99:
#         low = midpoint
#         return binary_search(low, high)
#     if percent_bouncy(midpoint) > 0.99:
#         high = midpoint
#         return binary_search(low, high)
#     if low == high:
#         return low

# print binary_search(1000000, 2000000)

bouncy = 0            # Number of bouncy numbers so far
total = 0               # Also functions as a counter
percent = 0              # Proportion of bouncy numbers

while percent < 0.99:
    total += 1
    if is_bouncy(total):
        bouncy += 1
    percent = float(bouncy) / total
    print total, percent
print total