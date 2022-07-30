# The problem of stack plates

class PlatesStack():
    def __init__(self, capasity):
        self.capasity = capasity
        self.stacks = []
    
    def __str__(self):
        return self.stacks

    def push(self, item):
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capasity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])
    
    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0 :
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()
    
    def pop_at(self, stackNum):
        if len(self.stacks[stackNum]) > 0:
            return self.stacks[stackNum].pop()
        else:
            return None

customStack = PlatesStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.pop())
