def remove_edge(graph, source, dest):
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