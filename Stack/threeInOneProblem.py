class Multistack :
    def __init__(self, stacksize):
        self.numberstacks = 3
        self.custList = [0] * (stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stacksize

    def isFull(self, stacknum):
        return self.sizes[stacknum] ==  self.stacksize

    def isEmpty(self, stacknum):
        return self.sizes[stacknum] == 0  
    
    def indexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return 'The stack is full'
        else :
            self.sizes[stacknum] += 1
            self.custList[self.indexOfTop(stacknum)] = item

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return 'The stack is empty'
        else: 
            topElem = self.custList[self.indexOfTop(stacknum)]
            self.custList[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return topElem
    
    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return 'The stack is empty'
        else: 
            return  self.custList[self.indexOfTop(stacknum)]

customStack = Multistack(6)
customStack.push(1, 0)
customStack.push(2, 0)
customStack.push(2, 2)
customStack.push(2, 2)
print(customStack.isEmpty(1))
print(customStack.isFull(2))
print(customStack.peek(0))