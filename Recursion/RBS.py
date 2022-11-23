from typing import List
def rotatedBinarySeacrh(arr: List[int], target: int) -> int:
    return helper(arr, target, 0, len(arr)-1)

def helper(arr: List[int], target: int, start: int, end: int) -> int:
    if start > end:
        return
    
    mid = (start + end)//2

    if arr[mid] == target:
        return mid

    if arr[start] <= arr[mid]:
        if target >= arr[start] and target <= arr[mid]:
            return helper(arr, target, start, mid-1)
        return helper(arr, target, mid+1, end)
    
    if target >= arr[mid] and target <= arr[end]:
        return helper(arr, target, mid+1, end)
    return helper(arr, target, start, mid-1)

arr = [5,6,7,8,9,1,2,4]

print(rotatedBinarySeacrh(arr, 9))