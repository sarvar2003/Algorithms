from bellmanFordSSSP import Graph
from bellmanFordSSSP import g

def bellmanFord(graph):
    for node in graph.nodes:
        dist = {i : float("inf") for i in graph.nodes}
        dist[node] = 0

        for _ in range(graph.V - 1):
            for s, d, w in graph.graph:
                if dist[s] != float("inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in graph.graph:
            if dist[s] != float("inf") and dist[s] + w < dist[d]:
                print("The graph has a negative cycle")
                return

        graph.print_result(dist, node)

bellmanFord(g)
