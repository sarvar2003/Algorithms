# Disjoin Set class Python

class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in self.vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] == item:
            return item
        return self.find(self.parent[item])
    
    def union(self, x, y):
        xrep = self.find(x)
        yrep = self.find(y)

        if (xrep == yrep):
            return
        
        xrank = self.rank[xrep]
        yrank = self.rank[yrep]

        if xrank < yrank:
            self.parent[xrep] = yrep
        elif yrank < xrank:
            self.parent[yrep] = xrep
        else:
            self.parent[yrep] = xrep

            self.rank[xrep] += 1
    
vertices = {"A", "B", "C", "D", "E"}
ds = DisjointSet(vertices)
ds.union("A", "C")
ds.union("C", "B")
print(ds.find("B"))