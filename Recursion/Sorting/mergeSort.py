from typing import List

def mergeSort(arr: List[int]) -> List[int]:
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

def merge(first: List[int], second: List[int]) -> List[int]:
    p1 = 0
    p2 = 0


    n1 = len(first)
    n2 = len(second)

    mix = []
    while p1 < len(first) and p2 < len(second):
        if first[p1] < second[p2]:
            mix.append(first[p1])
            p1 += 1
        else:
            mix.append(second[p2])
            p2 += 1
            

    while p1 < len(first):
        mix.append(first[p1])
        p1 += 1
    
    while p2 < len(second):
        mix.append(second[p2])
        p2 += 1
    
    return mix

arr = [6,4,8,2,1,9,4,2,0]
print(mergeSort(arr))
