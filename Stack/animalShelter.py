class Queue():
    def __init__(self):
        self.cats = []
        self.dogs = []
    
    def enqueue(self, type, animal ):
        if type.upper() == 'CAT':
            self.cats.append(animal)
        elif type.upper() == 'DOG':
            self.dogs.append(animal)
    
    def dequeCat(self):
        if len(self.cats) == 0:
            return None
        else :
            cat = self.cats.pop(0)
            return cat
    
    def dequeDog(self):
        if len(self.dogs) == 0:
            return None
        else :
            dog = self.dogs.pop(0)
            return dog

    def dequeAny(self):
        if len(self.cats) == 0 :
            return self.dogs.pop(0)
        else :
            return self.cats.pop(0)

    
customQueue = Queue()
customQueue.enqueue('cat', 'cat1')
customQueue.enqueue('cat', 'cat2')
customQueue.enqueue('cat', 'cat3')
customQueue.enqueue('cat', 'cat4')
customQueue.enqueue('dog', 'dog1')
customQueue.enqueue('dog', 'dog2')
customQueue.enqueue('dog', 'dog3')
print(customQueue.dequeCat())
print(customQueue.dequeDog())
print(customQueue.dequeAny())





        