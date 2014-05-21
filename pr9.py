def pythagorean_triplet_sum(n):
    for a in xrange(1, n - 1):
        for b in xrange(a + 1, n):
            c = n - a - b
            if (a ** 2 + b ** 2 == c ** 2):
                print a * b * c, 'with a = %d, b = %d, and c = %d' % (a,b,c)

pythagorean_triplet_sum(1000)
