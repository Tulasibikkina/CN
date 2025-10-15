import sys
INF = sys.maxsize

def print_routing_table(distance, nodes):
    print("\nRouting Table at each node:")
    for i in range(len(nodes)):
        print(f"\nNode {nodes[i]}:")
        print("Destination\tDistance\tNext Hop")
        for j in range(len(nodes)):
            if i != j:
                next_hop = distance[i][j][1]
                
                print(f"{nodes[j]}\t\t{distance[i][j][0]}\t\t{next_hop}")

                
def distance_vector_routing(graph, nodes):
    n = len(nodes)
    
    distance = [[[INF, None] for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                distance[i][j] = [0, nodes[i]]
            elif graph[i][j] != 0:
                distance[i][j] = [graph[i][j], nodes[j]]
        updated = True
    while updated:
        updated = False
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if distance[i][k][0] + distance[k][j][0] < distance[i][j][0]:
                        distance[i][j][0] = distance[i][k][0] + distance[k][j][0]
                        distance[i][j][1] = distance[i][k][1]
                        updated = True
    
    print_routing_table(distance, nodes)


nodes = ['A', 'B', 'C', 'D']
graph = [
    [0, 1, 3, 0],
    [1, 0, 1, 4],
    [3, 1, 0, 2],
    [0, 4, 2, 0]
]
distance_vector_routing(graph, nodes)