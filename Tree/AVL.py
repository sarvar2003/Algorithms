class AVLNode:

    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
    
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    
    def preOrder(self, root) -> None:
        if not root:
            return None
        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)
    
    def inOrder(self, root) -> None:
        if not root:
            return None
        print(root.val)
        self.inOrder(root.left)
        self.inOrder(root.right)
    
    def postOrder(self, root) -> None:
        if not root:
            return None
        print(root.val)
        self.postOrder(root.left)
        self.postOrder(root.right)
    
    def levelOrder(self, root) -> None:
        if not root:
            return None
        else:
            queue = [root]
            
            while queue:
                node = queue.pop(0)

                print(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
    
    def search(self, root, val) -> bool:

        if not root:
            return False
        else:
            if root.val == val:
                return True
            elif val < root.val:
                if root.left.val == val:
                    return True
                else:
                    self.search(root.left)
            else:
                if root.right.val == val:
                    return True
                else:
                    self.search(root.right)
    
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def rotateRight(self, disbalancedNode):
        newRoot = disbalancedNode.left
        disbalancedNode.left = disbalancedNode.left.right
        newRoot.right = disbalancedNode

        disbalancedNode.height = 1 + max(self.getHeight(disbalancedNode.left), self.getHeight(disbalancedNode.right))
        newRoot.height = 1 + max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))

        return newRoot

    def rotateLeft(self, disbalancedNode):
        newRoot = disbalancedNode.right
        disbalancedNode.right = disbalancedNode.right.left
        newRoot.left = disbalancedNode

        disbalancedNode = 1  + max(self.getHeight(disbalancedNode.left), self.getHeight(disbalancedNode.right))
        newRoot.height = 1 + max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))

        return newRoot
    
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left)-self.getHeight(root.right)
    
    def insert(self, root, val):
        if not root:
            return AVLNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and val < root.left.val:
            return self.rotateRight(root)

        if balance > 1 and val > root.left.val:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        if balance < -1 and val > root.right.val:
            return self.rotateLeft(root)

        if balance < -1 and val < root.right.val:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root
    
    def sucessor(self, root):
        current = root.right

        while current.left:
            current = current.left
        
        return current
    
    def predecessor(self, root):
        current = root.left

        while current.right:
            current = current.right
        
        return current
    
    def remove(self, root, val):

        if not root:
            return root
        else:
            if val < root.val:
                root.left = self.remove(root.left, val)
            elif val > root.val:
                root.right = self.remove(root.right, val)
            else:
                if not root.left and not root.right:
                    root = None
                    return root
                elif root.right:
                    root.val = self.sucessor(root)
                    root.right = self.remove(root.right, root.val)
                else:
                    root.val = self.predecessor(root)
                    root.left = self.remove(root.left, root.val)
            
            root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

            balance = self.getBalance(root)

            if balance > 1 and val < root.left.val:
                return self.rotateRight(root)
            
            if balance > 1 and val > root.left.val:
                root.left = self.rotateLeft(root.left)
                return self.rotateRight(root)
            
            if balance < -1 and val > root.right.val:
                return self.rotateLeft(root)
            
            if balance < -1 and val < root.right.val:
                root.right = self.rotateRight(root.right)
                return self.rotateLeft(root)

            return root
    
    def clear(self, root):
        root.val = None
        root.left = None
        root.right = None
        




avlTree = AVLNode(50)
avlTree.insert(avlTree, 25)
avlTree.insert(avlTree, 80)
avlTree.insert(avlTree, 35)

avlTree.remove(avlTree, 80)

avlTree.display()
# avlTree.levelOrder(avlTree)