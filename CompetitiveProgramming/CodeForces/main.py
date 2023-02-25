def solve(arr, maxn):
   if len(arr) == 0:
      return maxn
   a = arr.pop()
   if  a > maxn:
      maxn = a

   return solve(arr, maxn)

print(solve([1,2,3,4,6,67,8,7,56,3,3,4,6,5,3,2,4,6,5,2,2,6,53], -float("inf")))