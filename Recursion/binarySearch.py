# Binary search using recursion

def binarySearch(arr, target):
    return solve(arr, target, 0, len(arr)-1)

def solve(arr, target, start, end):
    if start > end:
        return -1

    mid = (start+end)//2

    if arr[mid] == target:
        return mid
    
    if arr[mid] > target:
        return solve(arr, target, start, mid-1)
    
    return solve(arr, target, mid+1, end)

arr = [1,4,7,12,15,18,25,37]

print(binarySearch(arr, 65446))