# Broadcast Tree using Dijkstra's Algorithm

import sys

def dijkstra(graph, source):
    n = len(graph)
    visited = [False] * n
    distance = [sys.maxsize] * n
    parent = [-1] * n

    distance[source] = 0

    for _ in range(n):
        # Find the unvisited node with the smallest distance
        min_dist = sys.maxsize
        u = -1
        for i in range(n):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        # Update distances of neighbors
        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                new_dist = distance[u] + graph[u][v]
                if new_dist < distance[v]:
                    distance[v] = new_dist
                    parent[v] = u

    return parent, distance


def print_broadcast_tree(parent, source):
    print("\n--- Broadcast Tree ---")
    for i in range(len(parent)):
        if i != source and parent[i] != -1:
            print(f"{parent[i]} → {i}")


# ----------------------------
# Main Program
# ----------------------------
if __name__ == "__main__":
    n = int(input("Enter number of hosts in subnet: "))
    print("Enter adjacency matrix (0 if no link):")
    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    source = int(input("Enter source host (0-indexed): "))

    parent, distance = dijkstra(graph, source)

    print_broadcast_tree(parent, source)

    print("\nShortest distance from source to each host:")
    for i in range(n):
        print(f"Host {source} → Host {i} = {distance[i]}")