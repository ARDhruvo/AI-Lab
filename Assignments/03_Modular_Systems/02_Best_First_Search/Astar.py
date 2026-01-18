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


def Astar_traversal(i, g, g_cost, pp):
    global pq, path, Graph, visited, g_costs

    if path:
        return

    visited.append(i)
    pp.append(i)

    if i == g:
        path = True
        print(f"Goal node {g} reached with path cost {g_cost}")
        print("Path taken:", " -> ".join(map(str, pp)))
        return

    for v in range(1, node_no + 1):
        if Graph[i][v] != math.inf and v not in visited:
            new_g_cost = g_cost + Graph[i][v]
            f_cost = new_g_cost + h[v]

            heapq.heappush(pq, (f_cost, new_g_cost, v, pp.copy()))

    while pq and not path:
        f_cost, current_g_cost, current_node, current_path = heapq.heappop(pq)

        if current_node in g_costs and current_g_cost >= g_costs[current_node]:
            continue

        g_costs[current_node] = current_g_cost

        Astar_traversal(current_node, g, current_g_cost, current_path)


def Astar():
    global pq, visited, path, g_costs
    pq = []
    visited = []
    path = False
    g_costs = {}

    start_node = int(input("Enter start node: "))
    goal_node = int(input("Enter goal node: "))

    g_costs[start_node] = 0

    Astar_traversal(start_node, goal_node, 0, [])


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
Astar()
