from typing import List

# Given an int array count the number of subsets whose sum equals to x


# Recursion approach
# Time complexity: 2^N
def countSubsetSum(nums: List[int], x: int, n: int) -> int:
    if x == 0:
        return 1
    if n == 0:
        return 0
    if nums[n-1] > x:
        return countSubsetSum(nums, x, n-1)
    else:
        return countSubsetSum(nums, x, n-1) + countSubsetSum(nums, x-nums[n-1], n-1)

# Top-Down approach 
# Time complexity: O(N*X)
def countSubsetSumDP(nums: List[int], x: int) -> int:
    n = len(nums)
    dp = [[0]*(x+1) for i in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1
    
    for j in range(1,x+1):
        dp[0][j] = 0
    

    for i in range(1, n+1):
        for j in range(1, x+1):
            if nums[i-1] > j:
                dp[i][j] == dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
        
    return dp[n][x]

print(countSubsetSum([3,1,2,3], 6, 4))
print(countSubsetSumDP([3,1,2,3], 6))