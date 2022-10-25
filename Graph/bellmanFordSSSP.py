import math
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.nodes = []
        self.graph = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)
    
    def print_result(self, dist, src:None):
        print("Vertex distance from source", src)
        for key, value in dist.items():
            if value == float("inf"):
                value = "N/A" 
            print(" " + key, " :  ", value)

def bellmanFord(graph, src):
    # Marking all distances infinity and src to 0
    dist = {i : math.inf for i in self.nodes}
    dist[src] = 0

    # iterating through graph to update distances when min is found
    for _ in range(graph.V - 1):
        for s, d, w in graph.graph:
            if dist[s] != math.inf and dist[s] + w < dist[d]:
                dist[d] = dist[s] + w
    
    # checking for a negative cycle
    for s, d, w in graph.graph:
        if dist[s] != math.inf and dist[s] + w < dist[d]:
            print("The graph contains negative cycle")
            return
    

    graph.print_result(dist)

g = Graph(5)
# Add nodes to graph
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
#  Add edges to graph
g.addEdge("A", "C", 6)
g.addEdge("A", "D", 6)
g.addEdge("B", "A", 3)
g.addEdge("C", "D", 1)
g.addEdge("D", "C", 2)
g.addEdge("D", "B", 1)
g.addEdge("E", "B", 4)
g.addEdge("E", "D", 2)

# g.bellmanFord("E")
