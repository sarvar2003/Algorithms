from typing import List

def quickSort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [i for i in arr[1:] if i < pivot]
        right = [i for i in arr[1:] if i >= pivot]

        return quickSort(left) + [pivot] + quickSort(right)

print(quickSort([2,3,3,2,3,4,4,56,4,43,46,7,7,45,324,2,46,78,89,67,45,4,4,6677,68,68,6,65,4,3,334,46,57,686,87,85,455,4,34,46,68,79,5,4,5,67,78667,5,6,5,9,7,5,2,1,4,6]))