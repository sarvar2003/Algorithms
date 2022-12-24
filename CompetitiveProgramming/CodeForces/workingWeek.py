t = int(input())
from itertools import permutations
from math import inf
for _ in range(t):
    n = int(input())
    
    week = [day for day in range(2,n-1)]
    p = permutations(week, 2)
    
    visited = {}

    mx = -inf

    for perm in p:
        first, second = perm
        if (first, second) not in visited or (second, first) not in visited:
            if abs(first-second) >= 2:
                l1 = abs(1-first)
                l2 = abs(second - first) - 1
                l3 = abs(n - second) - 1
                mx = max(mx, min(abs(l1-l2), abs(l2-l3), abs(l3-l1)))
                visited[(first, second)] = 1
                visited[(second, first)] = 1

    print(mx)



