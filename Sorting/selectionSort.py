def selectionSort(nums:list):
    for i in range(len(nums)):
        min_index = i
        for j in range(i, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


nums = [4,8,6,3,78,12,45,9,654,486531,351]
print(selectionSort(nums))
