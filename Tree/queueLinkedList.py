class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
    
class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)
    
    def isEmpty(self):
        return self.linkedlist.head == None

    def enqueue(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.linkedlist.head = newNode
            self.linkedlist.tail = newNode
        else :
            self.linkedlist.tail.next = newNode
            self.linkedlist.tail = newNode
    
    def dequeue(self):
        if self.isEmpty():
            return 'The queue has no element to delete'
        else:
            firstNode = self.linkedlist.head 
            if self.linkedlist.head == self.linkedlist.tail :
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next

            return firstNode
    
    def peek(self):
        if self.isEmpty():
            return 'The queue has no element to delete'
        else:
            return self.linkedlist.head

    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None


custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
# print(custQueue)
# # print(custQueue.peek())
# print(custQueue.dequeue())
# print(custQueue)
# print(custQueue.peek())
