from typing import List

def bubbleSort(arr: List[int], row: int, col: int) -> List[int]:
    if row == 0:
        return 
    
    if col < row:
        if arr[col] > arr[col+1]:
            temp = arr[col]
            arr[col] = arr[col+1]
            arr[col+1] = temp
        
        bubbleSort(arr, row, col+1)
    else:
        bubbleSort(arr, row-1, 0)
    
arr = [5,4,3,2,1,0,9]

bubbleSort(arr, len(arr)-1, 0)

print(arr)