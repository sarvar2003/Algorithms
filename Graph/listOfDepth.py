class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        if self.next is None:
            self.next = ListNode(val)
        else:
            self.next.add(val)
        
    def __str__(self):
        return "{val} -> ".format(val=self.val) + str(self.next)

    
class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth(tree):
    if tree is None:
        return 0
    
    if tree.left is None and tree.right is None:
        return 1
    depthLeft = 1 + depth(tree.left)
    depthRight = 1 + depth(tree.right)

    if depthLeft > depthRight:
        return depthLeft
    return depthRight

def treeToListnode(tree, custDict = {}, d=None):
    if d is None:
        d = depth(tree)
    
    if custDict.get(d) is None:
        custDict[d] = ListNode(tree.val)
    else:
        custDict[d].add(tree.val)
        if d == 1:
            return custDict
    if tree.left != None:
        custDict = treeToListnode(tree.left, custDict, d-1)
    if tree.right != None:
        custDict = treeToListnode(tree.right, custDict, d-1)
    
    return custDict

rootNode = Treenode(1)
two = Treenode(2)
three = Treenode(3)
four = Treenode(4)
five = Treenode(5)
six = Treenode(6)
seven = Treenode(7)

rootNode.left = two
rootNode.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

custDict = treeToListnode(rootNode)

for depth, listnode in custDict.items():
    print("Depth:{0} - Listnode :{1}".format(depth, listnode))
