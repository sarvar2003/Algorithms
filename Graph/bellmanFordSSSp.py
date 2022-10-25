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
    
    def print_result(self, dist):
        print("Vertex distance from source")
        for key, value in dist.items():
            print(" " + key, " :  ", value)

    def bellmanFord(self, src):
        # Marking all distances infinity and src to 0
        dist = {i : math.inf for i in self.nodes}
        dist[src] = 0

        # iterating through graph to update distances when min is found
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != math.inf and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        
        # checking for a negative cycle
        for s, d, w in self.graph:
            if dist[s] != math.inf and dist[s] + w < dist[d]:
                print("The graph contains negative cycle")
                return
        

        self.print_result(dist)

graph = Graph(5)
# Add nodes
graph.addNode("A")
graph.addNode("B")
graph.addNode("C")
graph.addNode("D")
graph.addNode("E")
#  Add edges
graph.addEdge("A", "C", 6)
graph.addEdge("A", "D", 6)
graph.addEdge("B", "A", 3)
graph.addEdge("C", "D", 1)
graph.addEdge("D", "C", 2)
graph.addEdge("D", "B", 1)
graph.addEdge("E", "B", 4)
graph.addEdge("E", "D", 2)

graph.bellmanFord("E")
