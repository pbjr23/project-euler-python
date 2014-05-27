def get_permutations(l): 
    if len(l) == 1: 
        yield l 
    else: 
        for i in range(len(l)): 
            head = l[i] 
            tail = l[:i] + l[i+1:] 
            for x in get_permutations(tail): 
                yield [head] + x

def nth_permutation(l, n):
    count = 0
    for permutation in get_permutations(l):
        count += 1
        if count == n:
            return int(''.join([str(x) for x in permutation]))

print nth_permutation([0,1,2,3,4,5,6,7,8,9], 1000000)
