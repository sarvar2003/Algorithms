def bubbleSort(custList):
    for i in range(len(custList)-1):
        for j in range(len(custList)-i-1):
            if custList[j] > custList[j+1]:
                custList[j], custList[j+1] = custList[j+1], custList[j]
    
    return custList

print(bubbleSort([1,4,7,5,3,9,6]))

