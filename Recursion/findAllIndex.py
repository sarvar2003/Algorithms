#  Find all the indexes of the target and return as a list
from typing import List

def findAllIndex(arr : List[int], target: int) -> List[int]:
    res = [] 
    return helper(arr, target, 0, res)

def helper(arr: List[int], target: int, index: int, res: List[int]) -> List[int]:
    if index == len(arr):
        return res 
    
    if arr[index] == target:
        res.append(index)
    
    return helper(arr, target, index+1, res)

arr = [1,3,6,7,9,1,6]
print(findAllIndex(arr, 1))