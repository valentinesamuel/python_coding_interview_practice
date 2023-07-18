def is_tree(graph):
    visited = [False] * graph.vertices

    # Check for cycles using depth-first search
    if has_cycle(graph, visited, 0, -1):  # Start from vertex 0, assuming an undirected graph
        return False

    # Check if all vertices are visited (graph is connected)
    for vertex in visited:
        if not vertex:
            return False
    return True


def has_cycle(graph, visited, vertex, parent):
    visited[vertex] = True

    # Traverse the neighbors of the current vertex
    for neighbor in graph.array[vertex]:
        if not visited[neighbor]:
            # Recursively check for cycles in the neighbor's subtree
            if has_cycle(graph, visited, neighbor, vertex):
                return True
        elif neighbor != parent:
            # If the neighbor is already visited and not the parent, there is a cycle
            return True

    return False
