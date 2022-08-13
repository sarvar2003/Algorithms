class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def preorder(self, root):
        if not root:
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.value)
        self.inorder(root.right)

    def insert(self, root, value):
        if not root:
            root = BST(value)
        else:
            if value < root.value:
                if root.left is None:
                    root.left = BST(value)
                else:
                    self.insert(root.left, value)
            else:
                if root.right is None:
                    root.right = BST(value)
                else:
                    self.insert(root.right, value)
    
    def getMinNode(self, root):
        if not root:
            return None
        
        current = root

        while current.left:
            current = current.left
        
        return current

    def remove(self, root, value):

        if not root:
            return root
        elif root.value > value:
            root.left = self.remove(root.left, value)
        elif root.value < value:
            root.right = self.remove(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root.right = None
                return temp
            
            if root.right is None:
                temp = root.left
                root.left = None
                return temp
            
            temp = self.getMinNode(root.right)
            root.value = temp.value
            root.right = self.remove(root.right, temp.value)
        return root
    
    def clear(self, root):
        root.value = None
        root.left = None
        root.right = None


            


bst = BST(10)
bst.insert(bst, 5)
bst.insert(bst, 20)
bst.insert(bst, 40)
bst.insert(bst, 8)
bst.insert(bst, 18)
bst.remove(bst, 20)
bst.remove(bst, 40)
bst.preorder(bst)
# print(bst.getMinNode(bst).value)