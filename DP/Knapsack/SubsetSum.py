from typing import List


# Recursive approach
# Time complexity 2^N
def subsetSumRec(nums: List[int], target: int, n: int) -> bool:
    if target == 0:
        return True
    
    if n == 0 and sum != 0:
        return False
    
    if nums[n-1] > target:
        return subsetSumRec(nums, target, n-1)
    else:
        return subsetSumRec(nums, target, n-1) or subsetSumRec(nums, target - nums[n-1], n-1)


# Top-down approach
# Time complexity O(N*T)
def subsetSum(nums: List[int], target: int) -> bool:
    n = len(nums)
    dp = [[False]*(target + 1) for i in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True
    
    for j in range(1, target + 1):
        dp[0][j] = False
    

    for i in range(1, n+1):
        for j in range(1, target + 1):
            if nums[i-1] > j:
                dp[i][j] == dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        
    return dp[n][target]

print(subsetSum([1,2,3,4,7,7,8], 17))