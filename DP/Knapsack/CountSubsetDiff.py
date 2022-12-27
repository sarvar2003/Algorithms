# Count the number of ways to divide an array into two such that their difference is equal to X

from typing import List

def countSubsetDIff(nums: List[int], x: int) -> int:
    S1 = (sum(nums)-x)//2

    # Now its count subset sum problem with target being S1

    n = len(nums)
    dp = [[0]*(S1+1) for i in range(n+1)]

    for j in range(S1+1):
        dp[0][j] = 0

    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, S1+1):
            if nums[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
    
    return dp[n][S1]

print(countSubsetDIff([1,3,2,3], 3))