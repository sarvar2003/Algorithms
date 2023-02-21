from typing import List

# Recursive approach
def RecursiveMCM(matrices: List[int]) -> int:
    return recursive(matrices, 1, len(matrices)-1)

def recursive(matrices: List[int], left: int, right: int) -> int:
    if left >= right:
        return 0
    ans = float("inf")

    for k in range(left, right):
        leftSide = recursive(matrices, left, k) 
        rightSide = recursive(matrices, k+1, right) 
        cost = matrices[left-1]*matrices[k]*matrices[right]

        curr = leftSide + rightSide + cost

        ans = min(ans, curr)

    return ans

# print(MCM([1,2,3,4]))

# Memoization approach
def MemoizationMCM(matrices: List[int]) -> int:
    n = len(matrices) 
    memo  = [[-1 for _ in range(100)] for _ in range(100)]
    

    def memoization(left: int, right: int) -> int:
        if left == right:
            return 0
        
        if memo[left][right] != -1: 
            return memo[left][right]
        
        memo[left][right] = float("inf")
        for k in range(left, right):
            memo[left][right] = min(memo[left][right], memoization(left, k) + memoization(k+1, right) + matrices[left-1]*matrices[k]*matrices[right])
        
        return memo[left][right] 
    
    return memoization(1, n-1)

print(MemoizationMCM([10,20,30,40]))

def TabulationMCM(matrices: List[int]) -> int:
    n = len(matrices)
    dp = [[-1]*(n) for _ in range(n)]

    for cl in range(2, n):
        for left in range(1, n-cl+1):
            right = left + cl - 1
            dp[left][right] = float("inf")

            for k in range(left, right):
                totalCost = dp[left][k] + dp[k+1][right] + matrices[left-1]*matrices[k]*matrices[right]

                dp[left][right] = min(dp[left][right], totalCost)

    return dp[1][-1]

print(TabulationMCM([1,2,3,4]))
