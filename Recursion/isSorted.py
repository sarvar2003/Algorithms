from typing import List

def isSorted(arr : List[int], index: int) -> bool:
    if index == len(arr) - 1 :
        return True
    
    if arr[index] > arr[index + 1]:
        return False
    return  isSorted(arr, index + 1)


print(isSorted([1,2,4,6,7,9], 0))