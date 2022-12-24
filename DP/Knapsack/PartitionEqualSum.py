from typing import List
from SubsetSum import subsetSumRec

# Recursive approach
# Time complexity: 2^N
def partitionEqualsSumRec(nums: List[int]) -> bool:
    # Nums set with odd sum cannot be devide into two equal subsets
    if sum(nums) % 2 == 1:
        return False

    target = sum(nums)/2
    n = len(nums)

    return subsetSumRec(nums, target, n)


# Top-Down approach
# Time complexity: O(N*T) T is sum(nums) divided by 2 

def partitionEqualsSum(nums: List[int]) -> bool:
    
    if sum(nums) % 2 == 1:
        print("afsd")
        return False

    target = sum(nums)//2
    n = len(nums)

    dp = [[False]*(target+1) for i in range(n+1)]

    for i in range(n+1):
        dp[i][0] = False
    
    for j in range(1, target + 1):
        dp[0][j] = False
    

    for i in range(1, n+1):
        for j in range(1, target + 1):
            if nums[i-1] > j:
                dp[i][j] = dp[i-1][j]
            elif nums[i-1] == j:
                dp[i][j] = True
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

    return dp[n][target]   

print(partitionEqualsSum([1,5,10,6]))
