def solve():
   steps = int(input()) 
   five = steps // 5
   steps = steps % 5
   four = steps // 4
   steps = steps % 4
   three = steps // 3
   steps = steps % 3
   two = steps // 2
   steps = steps % 2
   one = steps//1

   print(five + four + three + two + one)

solve()