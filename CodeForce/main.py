class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printPath(root):
    path = []
    printPathRec(root, path, 0)
    
def printPathRec(root, path, pathLen):
    
    if root is None :
        return
    
    
    if len(path) > pathLen:
        path[pathLen] = root.val
    else:
        path.append(root.val)
        
    if root.left is None and root.right is None:
        printArray(path, pathLen)
    else:
        printPathRec(root.left, path, pathLen)
        printPathRec(root.right, path, pathLen)
        
def printArray(ints, len):
    for i in ints[0 : len]:
        print(i," ",end="")
        print()
        
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
paths = Paths(root)
printArray(paths)