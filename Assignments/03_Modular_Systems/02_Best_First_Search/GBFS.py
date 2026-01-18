import heapq
import math

# Global Variables


Graph = [[]]
h = {}

nodes = []

pq = []  # priority queue
path = False
visited = []

node_no = 0
edge_no = 0

# Functions


def print_Graph():
    print("Adjacency Matrix:\n")
    print("\t", end="")
    for i in range(1, node_no + 1):
        print(f"{i}\t", end="")

    for i in range(1, node_no + 1):
        print(f"\n{i}\t", end="")
        for j in range(1, node_no + 1):
            if Graph[i][j] == math.inf:
                print("INF\t", end="")
            else:
                print(f"{Graph[i][j]}\t", end="")
    print()

    print("\nHeuristic Values:")
    for u in nodes:
        print(f"h({u}) = {h[u]}")
    print()


def save_Graph():
    graph = open("graph.txt", "w")
    print(node_no, 2 * edge_no, file=graph)
    for i in range(1, node_no + 1):
        for j in range(1, node_no + 1):
            if Graph[i][j] != math.inf:
                print(i, j, Graph[i][j], file=graph)

    for u in nodes:
        print(f"{u} {h[u]}", file=graph)
    graph.close()


def read_Graph():
    global node_no, edge_no, Graph
    graph = open("graph.txt", "r")
    node_no, edge_no = map(int, graph.readline().split())
    Graph = [[math.inf for _ in range(node_no + 1)] for _ in range(node_no + 1)]
    for _ in range(edge_no):
        u, v, c = map(int, graph.readline().split())
        Graph[u][v] = c

    for _ in range(node_no):
        u, hv = map(int, graph.readline().split())
        h[u] = hv
        if u not in nodes:
            nodes.append(u)
    graph.close()


def GBFS_traversal(i, g, cost, pp):
    global pq, path, Graph, visited
    if path or i in visited:
        return
    else:
        pp.append(i)
        visited.append(i)
        if i == g:
            path = True
            print(f"Goal node {g} reached with path cost {cost}")
            print("Path taken:", " -> ".join(map(str, pp)))
            return
        else:
            for v in range(len(Graph[i])):
                if Graph[i][v] != math.inf:
                    heapq.heappush(pq, (Graph[i][v], v))
                while pq and not path:
                    current_cost, current_node = heapq.heappop(pq)
                    GBFS_traversal(current_node, g, cost + current_cost, pp)


def GBFS():
    global pq, visited, path
    pq = []
    visited = []
    start_node = int(input("Enter start node: "))
    goal_node = int(input("Enter goal node: "))

    GBFS_traversal(start_node, goal_node, 0, [])


def input_Graph():
    global node_no, edge_no, Graph, nodes
    node_no, edge_no = map(int, input("Enter number of nodes and edges: ").split())
    Graph = [[math.inf for _ in range(node_no + 1)] for _ in range(node_no + 1)]

    print("Enter connections and cost:")
    for i in range(edge_no):
        u, v, c = map(int, input().split())
        if u not in nodes:
            nodes.append(u)
        if v not in nodes:
            nodes.append(v)
        Graph[u][v] = c
        Graph[v][u] = c  # For undirected graph

    for u in nodes:
        h[u] = int(input(f"Enter heuristic value for node {u}: "))


# Main

input_Graph()
save_Graph()
read_Graph()
print_Graph()
GBFS()
