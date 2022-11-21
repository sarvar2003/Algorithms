class Treenode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
    
def leftmostNode(node):
    current = node
    while current:
        if current.left is None:
            break
        current = current.left
    return current

def inOrderSuccessor(root, node):
    if node.right:
        return leftmostNode(node.right)
    
    p = node.parent
    while p:
        if node != p.right:
            break
        
        node = p
        p = p.parent
    return p 

def insert(node, data):
    if not node:
        return Treenode(data)
    
    if data <= node.val:
        temp = insert(node.left, data)
        node.left = temp
        temp.parent = node
    else:
        temp = insert(node.right, data)
        node.right = temp
        temp.parent = node
    
    return node

root = None
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 8)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 5)
root = insert(root, 9)

temp = root.right

successor = inOrderSuccessor(root, temp)

if successor:
    print("The successor of %d is %d" %(temp.val, successor.val))
else:
    print("The successor of the node does not exist.")

