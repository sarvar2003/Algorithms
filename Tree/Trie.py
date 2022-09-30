class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode() 

    def insertString(self, word: str):
        curr = self.root
        for char in word:
            node = curr.children.get(char)
            if node is None:
                node = TrieNode()
                curr.children.update({char:node})
            curr = node
        curr.endOfString = True
    
    def searchString(self, word):
        curr = self.root
        for char in word:
            node = curr.children.get(char)
            if node is None:
                return False
            curr = node
        
        return curr.endOfString 


def deleteString(root, word, index):
    char = word[index]
    currNode = root.children.get(char)
    canBeDeleted = False

    if len(currNode.children) > 1:
        deleteString(root, word, index+1)
        return False
    
    if index == len(word) - 1:
        if len(currNode.children) > 0:
            currNode.endOfString = False
            return False
        else :
            root.children.pop(char)
            return True

    if currNode.endOfString:
        deleteString(currNode, word, index+1)
        return False

    canBeDeleted = deleteString(currNode, word, index+1)

    if canBeDeleted:
        root.children.pop(char)
        return True
    else:
        return False     
    

newTrie = Trie()
newTrie.insertString('App')
newTrie.insertString('Appl')
deleteString(newTrie.root, 'App', 0)
print(newTrie.searchString('App'))
