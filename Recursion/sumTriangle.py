def sumTriangle(arr):
    if len(arr) == 1:
        print(arr)
        return 
    
    sumArr = []

    for i in range(len(arr)-1):
        sumArr.append(arr[i] + arr[i+1])
    
    sumTriangle(sumArr)
    print(arr)  

sumTriangle([1, 2, 3, 4, 5])