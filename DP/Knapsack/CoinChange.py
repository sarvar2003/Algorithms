from typing import List
# This problem is a classic example of unbounded knapsack

# DP tabulation approach
# Time complexity: O(N*M)
def coinChange(coins: List[int], amount: int) -> int:
    n = len(coins)

    dp = [[0]*(amount+1) for i in range(n+1)]

    for j in range(1,amount+1):
        dp[0][j] = float("inf")
    
    for i in range(1, n+1):
        for j in range(1, amount+1):
            if coins[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-coins[i-1]])
    
    return -1 if dp[n][amount] == float("inf") else dp[n][amount]

print(coinChange([1,2,5], 11))