class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict 
    
    def routeBetweenNodes(self, start, end):
        visited = [start]
        queue = [start]
        path = False

        while queue:
            deVertex = queue.pop(0)
            
            for adjacent in self.gdict[deVertex]:
                if adjacent not in visited:
                    if adjacent == end:
                        return True
                    else:
                        visited.append(adjacent)
                        queue.append(adjacent)
        return False

custDict = {
    "a" : ['c', 'd', 'b'],
    "b" : ["j"],
    "c" : ["g"],
    "g" : ["h"],
    "e" : ["f", "a"],
    "f" : ["i"],
    "d" : [],
    "h" : [],
    "j" : [],
    "i" : [],
}

g = Graph(custDict)
print(g.routeBetweenNodes("a", "h"))