def mergeSort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2

    right = mergeSort(arr[0: mid])
    left = mergeSort(arr[mid: len(arr)])

    return merge(left, right, mid)

def  merge(left, right, mid):
    i = 0
    j = 0

    mix = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            mix.append(left[i])
            i += 1
        else:
            mix.append(right[j])
            j += 1

    
    while i < len(left):
        mix.append(left[i])
        i += 1
    
    while j < len(right):
        mix.append(right[j])
        j += 1
    
    return mix

print(mergeSort([5,4,3,2,1]))