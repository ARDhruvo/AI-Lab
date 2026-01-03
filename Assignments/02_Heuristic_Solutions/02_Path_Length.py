def path_length(src, dst):
    if src == dst:
        return 0
    for edge in Edge:
        if edge[0] == src and edge[1] == dst:
            return edge[2]

    for edge in Edge:
        if edge[0] == src:
            adj_node = edge[1]
            if adj_node not in visited:
                visited.append(adj_node)
                cost = path_length(adj_node, dst)
                if cost != -1:
                    return edge[2] + cost
    return -1


# Main

# Graph
Edge = [
    ("i", "a", 35),
    ("i", "b", 45),
    ("a", "c", 22),
    ("a", "d", 32),
    ("b", "d", 28),
    ("b", "e", 36),
    ("b", "f", 27),
    ("c", "d", 31),
    ("c", "g", 47),
    ("d", "g", 30),
    ("e", "g", 26),
]

visited = []

src, dst = input("Enter Source and Destination: ").split()
print("Cost = ", path_length(src, dst))
