from typing import List

def quickSort(nums: List[int], low, high):
    if low >= high:
        return

    start = low
    end = high
    mid = end - (end - start) // 2

    pivot = nums[mid]

    while start <= end:
        while nums[start] < pivot:
            start += 1
        
        while nums[end] > pivot:
            end -= 1
        
        if start <= end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
        
    quickSort(nums, low, end)
    quickSort(nums, start, high)

nums = [1,2,5,7,9,23,1,5,6,7,4,2,7,0,5,2,1]
print(sorted(nums))
print("---------------------------")
quickSort(nums, 0, len(nums) - 1)
print(nums)