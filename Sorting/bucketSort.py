import math

def bucketSort(nums):
    numberOfBuckets = round(math.sqrt(len(nums)))
    maxValue = max(nums)
    temp = []

    for bucket in range(numberOfBuckets):
        temp.append([])
    
    for num in nums:
        index_b = math.ceil(num*numberOfBuckets/maxValue)
        temp[index_b-1].append(num)

    for bucket in temp:
        bucket.sort()

    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(temp[i])):
            nums[k] = temp[i][j]
            k += 1
    
    return nums

nums = [1, 7,2,5,3,90,10]

print(bucketSort(nums))
        

