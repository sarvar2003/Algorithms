# Coin change problem
from typing import List

def coinChange(totalChange: int, coins: List[int]):
    count = 0
    coins.sort()

    while totalChange > 0:
        if coins[-1] <= totalChange:
            n = totalChange // coins[-1]
            totalChange = totalChange % coins[-1]
            print(str(n) + " " + str(coins[-1]))
        else:
            coins.pop()
    

coins = [1,2,5,10,100,1000]
coinChange(2035, coins)