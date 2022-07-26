from sys import maxsize


class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list ]
        return '\n'.join(values)

    def isEmpty(self):
        return self.list == []

    def isFull(self):
        return len(self.list) == self.maxSize
    
    def push(self, value):
        if self.isFull():
            return 'The stack is full'
        else :
            self.list.append(value)
            return 'The element has been successfully added'

    def pop(self):
        if self.isEmpty():
            return 'There is no element to pop'
        else :
            return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return 'There is no element to pop'
        else :
            return self.list[-1]
    
    def delete(self):
        self.list = None
            
customStack = Stack(4)
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
 
print(customStack.isFull())
print(customStack)


