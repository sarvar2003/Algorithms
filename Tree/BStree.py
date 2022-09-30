import queueLinkedList as queue
class BSTnode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    

def insertNode(rootNode, nodeValue):
    if rootNode is None:
        rootNode.data = nodeValue
    elif rootNode.data >= nodeValue:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTnode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTnode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return 'The node has been successfully inserted.'

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)

            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        

def searchNode(rootNode, nodeValue):
    if rootNode is None:
        return 
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild is not None:
            if rootNode.leftChild.data == nodeValue:
                print("The value is found")
            else:
                searchNode(rootNode.leftChild, nodeValue)
        
        else:
            searchNode(rootNode.rightChild, nodeValue)

    else:
        if rootNode.rightChild is not None:
            if rootNode.rightChild.data == nodeValue:
                print("The value is found")
            else:
                searchNode(rootNode.rightChild, nodeValue)
        
        else:
            searchNode(rootNode.leftChild, nodeValue)
        
def minNode(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild
    return current  

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if rootNode.data > nodeValue:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif rootNode.data < nodeValue:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = minNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return 'The BST has been successfully deleted'

newBST = BSTnode(70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)
print(deleteBST(newBST))
# newBST.leftChild.data
# newBST.rightChild.data
levelOrderTraversal(newBST)
# print(searchNode(newBST, 780))