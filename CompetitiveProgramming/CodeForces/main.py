def solve(nine, ten, n):
   atNine, atTen, cnt = {}, {}, 0

   for i in range(n):
      atNine[nine[i]] = i
   
   for i in range(n):
      atTen[ten[i]] = i

   # print(atNine, atTen)

   for i in range(n-1):
      if atNine[nine[i]] < atTen[nine[i+1]] and atNine[nine[i]] != atTen[nine[i]]:
         cnt += 1

   return cnt


for _ in range(int(input())):
   n = int(input())
   a = list(map(int, input().split()))
   b = list(map(int, input().split()))

   print(solve(a, b, n) )

"""
5
1 4 2 5 3
1 3 4 2 5
"""