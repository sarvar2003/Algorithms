# Zero  one knapsak basically means that youhave to options in terms of items. You can either take it as a whole 
# or skip it. After that you will proceed with the one which returns the max profit/value. 

from typing import List



# Time complexity: 2^N


def zeroOneKnapsack(weights: List[int], values: List[int], capacity: int, n: int) -> int: # n is the index of the item 
    if n == 0 or capacity == 0:
        return 0
    
    if weights[n] > capacity:
        return zeroOneKnapsack(weights, values, capacity, n-1) # Skip when capacity is less than weight of nth elem
    else:
        return max(
            zeroOneKnapsack(weights, values, capacity, n-1),
            values[n] + zeroOneKnapsack(weights, values, capacity - weights[n], n-1)
        ) # proceed with max of skip and take call



# Zero one knapsack problem using memoization
# Time complexity: O(W*N)
def zeroOneKSMem(weights: List[int], values: List[int], capacity: int, n: int, memo: dict) -> int:
    if capacity == 0 or n == 0:
        return 0
    
    key = (capacity, n)
    if key in memo:
        return memo[key]
    
    if weights[n] > capacity:
        memo[key] = zeroOneKSMem(weights, values, capacity, n-1, memo)
    else:
        memo[key] = max(zeroOneKSMem(weights, values, capacity, n-1, memo), values[n] + zeroOneKSMem(weights, values, capacity - weights[n], n-1, memo))
    
    return memo[key]


# Zero One Kanpsack problem using Top-Down approach 
# # Time complexity: O(W*N)

def zeroOneKSTopDown(weights: List[int], values: List[int], capacity: int, n: int, DPtable: List[List[int]]) -> int: 
    for i in range(n+1):
        for j in range(capacity+1):
            if i == 0 or j == 0:
                DPtable[i][j] = 0
            elif weights[i-1] > j:
                DPtable[i][j] = DPtable[i-1][j]
            else:
                DPtable[i][j] = max(DPtable[i-1][j], values[i-1] + DPtable[i-1][j - weights[i-1]])

    return DPtable[i][j]


weights = [2,4,5,8,7,3]
values = [24,30,15,45,20,34]

dpTable = [[-1]*8 for i in range(7)]

print(zeroOneKnapsack(weights, values, 7, 5))
print(zeroOneKSMem(weights, values, 7, 5, {}))
print(zeroOneKSTopDown(weights, values, 7, 6, dpTable))
