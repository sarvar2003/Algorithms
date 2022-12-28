# Count the number of ways you can sum up the given amount using given coins
from typing import List

def coinChangeCount(coins: List[int], amount: int) -> int:
    n = len(coins)

    dp = [[0]*(amount+1) for i in range(n+1)]

    for i in range(n+1):
        for j in range(amount+1):
            if j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = 0
            elif coins[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]

    return dp[n][amount]

print(coinChangeCount([1,2,5], 5))