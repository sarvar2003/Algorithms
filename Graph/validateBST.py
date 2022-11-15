class Treenode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def helper(node, minValue = float('-inf'), maxValue = float('inf')):
    if not node:
        return True
    
    val = node.val
    
    if val <= minValue or val >= maxValue:
        return False
    
    if not helper(node.right, val, maxValue):
        return False
    
    if not helper(node.left, minValue, val):
        return False
    
    return True

def validateBST(root):
    return helper(root)

root1 = Treenode(2)
root1.left = Treenode(1)
root1.right = Treenode(4)
print(validateBST(root1))


root2 = Treenode(5)
root2.left = Treenode(6)
root2.right = Treenode(3)
print(validateBST(root2))