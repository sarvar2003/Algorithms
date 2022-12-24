"""
So, you've decided to stick to the following strategy to avoid suspicions: you take the minimum number of coins, 
whose sum of values is strictly more than the sum of values of the remaining coins.
On this basis, determine what minimum number of coins you need to take to divide them in the described manner.
"""

n = input()
coins = [int(i) for i in input().split()]

coins.sort(reverse=True)

totalSum = sum(coins)
currSum, count = 0, 0
while currSum <= totalSum - currSum:
    currSum += coins[count]
    count += 1

print(count)