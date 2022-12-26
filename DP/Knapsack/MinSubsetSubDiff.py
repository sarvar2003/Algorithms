# Find min difference between subsets of an array if divided into two subsets

from typing import List
import math
def minSubsetDif(nums: List[int]) -> int:
    totalSum = sum(nums)
    n = len(nums)

    dp = [[False]*(totalSum + 1) for i in range(n+1)]

    for i in range(n+1):
        for j in range(totalSum + 1):
            if j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            elif j < nums[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

    diff = math.inf
    for i in range(totalSum//2 + 1):
        first = i
        second = totalSum - i
        if dp[n][i] == True and diff > abs(first - second):
            diff = abs(first - second)

    return diff 

print(minSubsetDif([2,3,2,4]))