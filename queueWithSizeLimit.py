class Queue():
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        return (self.top + 1 == self.start) or ( self.start == 0 and self.top + 1 == self.maxSize )

    def isEmpty(self):
        return self.top == -1
    
    def enqueue(self, value):
        if self.isFull():
            return 'The queue is full'
        else :
            if self.top + 1 == self.maxSize:
                self.top = 0 
            else:
                self.top += 1
                if self.start == -1 :
                    self.start = 0
            self.items[self.top] = value
            return 'The element has been successfully added to the end of the queue'

    def dequeue(self):
        if self.isEmpty():
            return 'The queue is empty'
        else :
            firstElelement = self.items[self.start]
            start = self.start
            if self.top == self.start :
                self.top = -1
                self.start = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else : 
                self.start += 1
            self.items[start] = None
            return firstElelement 

    def peek(self):
        if self.isEmpty():
            return 'There is no element'
        else: 
            return self.items[self.start]
    
    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1


customQueue = Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
customQueue.dequeue()
print(customQueue.isFull())
# print(customQueue.peek())
customQueue.delete()
print(customQueue)
print(customQueue.isEmpty())