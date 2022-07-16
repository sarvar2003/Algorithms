class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        return self.LinkedList.head == None
    
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    
    def pop(self):
        if self.isEmpty() :
            return "There is no element to pop"
        else :
            nodeVal = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeVal
        
    def peek(self):
        if self.isEmpty() :
            return "There is no element to pop"
        else :
            nodeVal = self.LinkedList.head.value
            return nodeVal
    
    def delete(self):
        self.LinkedList.head = None



customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
# print(customStack.pop())
print(customStack.peek())
print('-----------')
# print(customStack.isEmpty())
print(customStack)