def isBalancedHelper(root):
    if not root:
        return 0

    leftHeight = isBalancedHelper(root.left)
    if leftHeight == -1:
        return -1
    
    rightHeight = isBalancedHelper(root.right)
    if rightHeight == -1:
        return -1

    if abs(rightHeight - leftHeight) > 1:
        return -1

    return max(rightHeight, leftHeight) + 1

def isBalanced(root):
    return isBalancedHelper(root) > -1

class Node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

n1 = Node("N1")
n2 = Node("N2")
n3 = Node("N3")
n4 = Node("N4")
n5 = Node("N5")
n6 = Node("N6")
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6

print(isBalanced(n1))
