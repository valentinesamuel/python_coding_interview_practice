def is_tree(graph):
    """
    PROBLEM: Here's the basic difference between a graph and a tree. A graph can only be a tree under two conditions:
    - There are no cycles.
    - The graph is connected.
    
    A graph is connected when there is a path between every pair of vertices. In a connected graph, there are no unreachable vertices. Each vertex must be connected to every other vertex through either a direct edge or a graph traversal.

    Input: An u directed graph.

    Output: Returns True if the given graph is a tree. Otherwise, it returns False.

    Example Input:
    >>Adjacency List of Undirected Graph g1<<
    | 0 | => [ 3 ] -> [ 2 ] -> [ 1 ] -> None
    | 1 | => [ 0 ] -> None
    | 2 | => [ 0 ] -> None
    | 3 | => [ 4 ] -> [ 0 ] -> None
    | 4 | => [ 5 ] -> [ 3 ] -> None
    | 5 | => [ 4 ] -> None
    >>Adjacency List of Undirected Graph g2<<
    | 0 | => [ 3 ] -> [ 2 ] -> [ 1 ] -> None
    | 1 | => [ 0 ] -> None
    | 2 | => [ 3 ] -> [ 0 ] -> None
    | 3 | => [ 2 ] -> [ 0 ] -> None
    >>Adjacency List of Undirected Graph g3<<
    | 0 | => None
    | 1 | => None
    | 2 | => None
    | 3 | => None
    | 4 | => None
    | 5 | => None
    >>Adjacency List of Undirected Graph g4<<
    | 0 | => None

    Example Output:
    >>True
    >>False
    >>False
    >>True

    APPROACH:
    - Initial thoughts: I had no idea what to do

    - Plan: 
        - first of all, check for cycles
            - for each neighbor, if the neighbor has not been visited, the recursively, check the neighbors for cycles using the current node as a parent
            - else, if the neighbor has been visited, check that the neighbor is not the parent, to avoid false cycle detection
        - then check every item inthe visited array to see if any is False, if it is, that means, it was not visited and was not a neighbor of any node. 
        - If the neighbor is already visited and not the parent, there is a cycle
    """

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
