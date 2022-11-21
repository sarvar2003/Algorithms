from typing import List
def findMin(arr: List[int], n: int) -> int:
    if n == 1:
        return arr[0]
    
    return min(arr[n-1], findMin(arr, n-1))

def findMax(arr: List[int], n: int) -> int:
    if n == 1:
        return arr[0]
    
    return max(arr[n-1], findMax(arr, n-1))



arr = [1,5,4,-1,12,-5,17,26,-59]

print(findMin(arr, len(arr)))
print(findMax(arr, len(arr)))