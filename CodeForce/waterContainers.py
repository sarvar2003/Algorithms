class BSTnode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insertNode(rootNode, nodeValue):
        if rootNode is None:
            rootNode.data = nodeValue
        elif rootNode.data >= nodeValue:
            if rootNode.leftChild is None:
                rootNode.leftChild = BSTnode(nodeValue)
            else:
                insertNode(rootNode.leftChild, nodeValue)
        else:
            if rootNode.rightChild is None:
                rootNode.rightChild = BSTnode(nodeValue)
            else:
                insertNode(rootNode.rightChild, nodeValue)
 

def filledContainers(num_container, num_queries):
    customTree = BSTnode(1)
    
    for i in range(2, num_container - 1 ) :
        customTree.insertNode(i)
    
    




    

def main():

    T = int(input())
    num_container, num_queries = [int(i) for i in input().split('s')]

    ans = filledContainers(num_container, num_queries)

    print("Case #{}: {}".format(test_case, ans))


   


if __name__ == "__main__":
  main()