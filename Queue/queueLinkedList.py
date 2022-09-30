"""

Queue - using Linked List

"""
class Node:
  def __init__(self, nodeValue):
    self.val = nodeValue
    self.next = None

class LinkedList:
  def __init__(self, maxSize):
    self.head = None
    self.tail = None
    self.maxSize = maxSize
    self.size = 0
  
  def isFull(self):
    return self.size == self.maxSize
  
  def isEmpty(self):
    return self.head is None

  def append(self, nodeValue):
    if self.isFull():
      return
  
    node = Node(nodeValue)

    if self.isEmpty():
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node
    
    self.size += 1
  
  def popLeft(self):
    if self.isEmpty():
      return
    else:
      temp = self.head
      self.head = self.head.next
      self.size -= 1
      return temp.val
  
  def printLL(self):
    curr = self.head

    if not curr:
      print("Queue is empty")

    while curr:
      if curr.next:
        print(curr.val, end=" -> ")
      else:
        print(curr.val)
      curr = curr.next

class Queue:
  def __init__(self, maxSize: int):
    self.queue = LinkedList(maxSize)

  def isFull(self):
    return self.queue.isFull()

  def isEmpty(self):
    return self.queue.isEmpty()

  def enqueue(self, value):
    self.queue.append(value)
  
  def dequeue(self):
    self.queue.popLeft()
  
  def printQueue(self):
    self.queue.printLL()
    
    def peek(self):
        if self.queue.isEmpty():
            return 
        else:
            return self.queue.head

    def delete(self):
        self.queue.head = None
        self.queue.tail = None

custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue)
# print(custQueue.peek())
print(custQueue.dequeue())
print(custQueue)
print(custQueue.peek())
