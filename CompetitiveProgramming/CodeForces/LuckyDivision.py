"""
Petya calls a number almost lucky if it could be evenly divided by some lucky number(4, 7).
Help him find out if the given number n is almost lucky.
"""
n = int(input())

if n % 4 == 0 or n % 7 == 0:
    print("YES")
else:
    print("NO")