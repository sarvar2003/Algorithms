from typing import List

def isSorted(arr : List[int]) -> bool:
    if len(arr) == 1:
        return True
    
    if arr[0] > arr[1]:
        return False
    return  isSorted(arr[1:])


print(isSorted([10,2,4,6,7,9]))