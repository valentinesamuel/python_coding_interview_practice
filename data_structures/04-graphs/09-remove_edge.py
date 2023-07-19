def remove_edge(graph, source, dest):
    """
    PROBLEM: You must implement the remove_edge function which takes a source and a destination as arguments. If an edge exists between the two, it should be deleted.

    Input: A directed graph, a source (integer), and a destination (integer).

    Output: A directed graph with the edge between the source and the destination removed.

    Example Input:
    >>Adjacency List of Directed Graph<<
    Vertex	Edges
       0      1, 2
       1      3
       2      3, 4
       3      None
       4      0
    >>Adjacency List of Directed Graph<<
    Vertex	Edges
       0	1, 2
       1	3
       2	4
       3	None
       4	0

    Example Output:
    >>Removed
    >>Removed

    APPROACH:
    - Initial thoughts: I thought about traversing the linked list of every node starting from the source node then calling the linked list delete method on the head node

    - Plan: 
        - since we have the source node and destination node, we can just get the linked list at the graph array in the source index and call delete with the destination
        
    """
    if len(graph.array) == 0:
        return graph
    if source >= len(graph.array) or source < 0:
        return graph
    if dest >= len(graph.array) or dest < 0:
        return graph
    # Delete by calling delete on head of LinkedList
    # Note: the delete method caters for if the edge does not exist
    graph.array[source].delete(dest)
    return graph