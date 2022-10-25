# Printing the result
INF = float("inf")
def printResult(num_vertices, distance):
    for i in range(num_vertices):
        for j in range(num_vertices):
            if distance[i][j] == INF :
                print( "N/A", end=" ")
            else:
                print(distance[i][j], end=" ")
        print(" ")

# Floyd Warshall algorithm
def floydWarshall(num_vertices, Graph):
    distance = Graph

    for viaX in range(num_vertices):
        for src in range(num_vertices):
            for destination in range(num_vertices):
                distance[src][destination] = min(distance[src][destination], distance[src][viaX] + distance[viaX][destination])

    printResult(num_vertices, distance)

Graph = [
    [0, 8, INF, 1],
    [INF, 0, 1, INF],
    [4, INF, 0, INF],
    [INF, 2, 9, 1]
]

floydWarshall(4, Graph)