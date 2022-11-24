from typing import List


def selectionSort(arr: List[int], row: int, col: int, maxIndex: int) -> List[int]: 
    if row == 0:
        return 
    
    if row > col:
        if arr[col] > arr[maxIndex]:
            selectionSort(arr, row, col+1, col)
        else:
            selectionSort(arr, row, col+1, maxIndex)
    else:
        temp = arr[row-1]
        arr[row-1] = arr[maxIndex]
        arr[maxIndex] = temp
        selectionSort(arr, row-1, 0, 0)

arr = [5,4,3,2,1,0,9,12]

selectionSort(arr, len(arr), 0, 0)

print(arr)