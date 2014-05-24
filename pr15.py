from mathtools import factorial

def num_routes(x, y):
    return factorial(x + y) / factorial(x) / factorial(y)

print num_routes(20, 20)