class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

# Inserting value 
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The binary tree is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1 
        return "The value has been successfully inserted"
# Searching for a node
    def searchNode(self, value):
        for i in range(len(self.customList)):
            if self.customList[i] == value:
                return "Success"
        return "Not Found"
# Traversals 
    # Pre Order Tarversal
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)

    # In Order Tarversal
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 
        self.inOrderTraversal(index * 2 )
        print(self.customList[index])
        self.inOrderTraversal(index * 2 +1)
    # Post Order traversal
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.customList[index])
    
    # Level Order Traversal
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex + 1):
            print(self.customList[i])

    # Delete a node from a binary tree
    def delteNode(self, value):
        if self.lastUsedIndex == 0:
            return 'There is no element to delete'
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been succesfully deleted"
    
    # Delete bianry tree
    def deleteBt(self):
        self.customList = None
        return 'The binary tree has been succesfully deleted'
        


newBt.insertNode('Drink')
newBt.insertNode('Hot')
newBt.insertNode('Cold')
newBt.insertNode('Coffee')
newBt.insertNode('Tea')
# newBt.levelOrderTraversal(1)
newBt.delteNode('Drink')
newBt.levelOrderTraversal(1)
