def solve(l, r, arr):
    if l > len(arr) or r < 1:
        return arr
    if l+1== r:
        arr[l], arr[r] = arr[r], arr[l]
    else:
        solve(l, r-1, arr)
        solve(l+1, r, arr)
    return arr

t = int(input())
for test in range(t):
    n, k = [int(i) for i in input().split(" ")]
    if n == 1:
        print(1)
        break
    arr = list(range(n+1))
    res = solve(1, n, arr)
    print(res[k])
    