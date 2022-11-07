import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [0 for column in range(vertices)
                      for row in range(vertices)]
    
    def printRes(self):
        print("Edge : Weight")
        for i in range(1, self.V):
            print(parent[i], "-", "\t", self.graph[i][parent[i]])

    def minKey(self, key, mstSet):

        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index
    
     