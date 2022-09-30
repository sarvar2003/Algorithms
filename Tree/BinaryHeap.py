class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapsize = 0
        self.maxSize = size + 1

def peakofHeap(rootNode):
    if not rootNode :
        return 
    return rootNode.customList[1]

def sizeofHeap(rootNode):
    if not rootNode:
        return 
    return rootNode.heapsize

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapsize + 1):
            print(rootNode.customList[i])

def heapifyTreeInsert(rootNode, index, heaptype):
    parentIndex = index // 2
    if index <= 1:
        return
    if heaptype == 'Min':
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp

        heapifyTreeInsert(rootNode, parentIndex, heaptype)
    elif heaptype == 'Max':
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp

        heapifyTreeInsert(rootNode, parentIndex, heaptype)

def insertNode(rootNode, nodeValue, heaptype):
    if rootNode.heapsize + 1 == rootNode.maxSize :
        return 'The Bonary Heap is full'
    rootNode.customList[rootNode.heapsize + 1] = nodeValue
    rootNode.heapsize += 1
    heapifyTreeInsert(rootNode, rootNode.heapsize, heaptype)
    return 'The value has been successfully added'

def heapifyTreeExtract(rootNode, index, heaptype):
    leftIndex = index * 2
    rightIndex = index * 2 +1
    swapChild = 0

    if rootNode.heapsize < leftIndex:
        return 
    elif rootNode.heapsize == leftIndex:
        if heaptype == 'Min':
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else : # Max
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return 
    else :
        if heaptype == 'Min':
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else : # Max
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        heapifyTreeExtract(rootNode, swapChild, heaptype)      
        
def extractNode(rootNode, heaptype):
    if rootNode.heapsize == 0:
        return
    else:
        extarctedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapsize]
        rootNode.customList[rootNode.heapsize] = None
        rootNode.heapsize -= 1
    return extarctedNode

def deleteHeap(rootNode):
    rootNode.customList = None


newHeap = Heap(5)
# print(peakofHeap(newHeap))
# print(sizeofHeap(newHeap))

insertNode(newHeap, 4 , 'Max')
insertNode(newHeap, 5 , 'Max')
insertNode(newHeap, 3 , 'Max')
insertNode(newHeap, 1 , 'Max')
# print(extractNode(newHeap, 'Max'))
deleteHeap(newHeap)
levelOrderTraversal(newHeap)