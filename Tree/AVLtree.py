import queueLinkedList as queue

class AVLnode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1
    

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

# insertion
def getHeight(rootNode):
    if not rootNode:
        return 0 
    return rootNode.height

def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode 
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def  getBalance(rootNode):
    if not rootNode:
        return 0 
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLnode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.data : #Left left condition
        return rightRotate(rootNode)
    if balance > 1  and nodeValue > rootNode.leftChild.data: # Left Right condition
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data: # Right Right condition
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data: # Right Left condition
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode

def getMinValue(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValue(rootNode.leftChild)

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return 'The AVL tree does not exist'
    elif rootNode.data > nodeValue:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif rootNode.data < nodeValue:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = getMinValue(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >= 0 :
        return leftRotate(rootNode)
    if balance <  -1 and getBalance(rootNode.rightChild) <= 0:
        return rightRotate(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0 :
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0 :
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode

def deleteAVLtree(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return 'The AVL tree has been successfully deleted'

newAVL = AVLnode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
newAVL = deleteNode(newAVL, 15)
print(deleteAVLtree(newAVL))
levelOrderTraversal(newAVL)
