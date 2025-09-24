import sys

def dijkstra(graph, start):
    """
    Compute shortest paths from start vertex to all other vertices
    :param graph: adjacency matrix of the graph
    :param start: starting vertex index
    """
    n = len(graph)
    visited = [False] * n
    distance = [sys.maxsize] * n
    distance[start] = 0

    for _ in range(n):
        # Pick the unvisited vertex with the smallest distance
        min_dist = sys.maxsize
        u = -1
        for i in range(n):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        # Update distances of adjacent vertices
        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]

    return distance

# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    print("Enter adjacency matrix (0 if no edge):")
    graph = []
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    start = int(input("Enter starting vertex (0-indexed): "))
    shortest_distances = dijkstra(graph, start)

    print("\nShortest distances from vertex", start, ":")
    for i, d in enumerate(shortest_distances):
        print(f"Vertex {i} -> {d}")
