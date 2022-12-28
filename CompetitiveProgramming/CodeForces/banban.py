def solve():

    n = int(input())

    print(n//2 + n%2)

    l, r = 1, 3*n

    while l < r:
        print(l,r)
        l += 3
        r -= 3

T = int(input())

for t in range(T):
    solve()