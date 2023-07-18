from DS_Classes.GraphClass import Graph
import sys
sys.path.append('../DS_Classes/')

def countBiDirectionalNodes(graph):
    """
    PROBLEM: You have to implement the num_edges() function which takes an undirected graph and computes the total number of bidirectional edges. An illustration is also provided for your understanding.

    Input: A directed graph.

    Output: Returns the number of unique edges in the graph.

    Example Input:
    >>Adjacency List of Directed Graph<<
    | 0 | => [ 5 ] -> [ 2 ] -> None
    | 1 | => None
    | 2 | => [ 4 ] -> [ 3 ] -> [ 0 ] -> None
    | 3 | => [ 6 ] -> [ 5 ] -> [ 2 ] -> None
    | 4 | => [ 6 ] -> [ 2 ] -> None
    | 5 | => [ 6 ] -> [ 3 ] -> [ 0 ] -> None
    | 6 | => [ 4 ] -> [ 8 ] -> [ 7 ] -> [ 3 ] -> [ 5 ] -> None
    | 7 | => [ 8 ] -> [ 6 ] -> None
    | 8 | => [ 7 ] -> [ 6 ] -> None
    >>Adjacency List of Directed Graph<<
    | 0 | => None
    | 1 | => [ 3 ] -> [ 2 ] -> None
    | 2 | => [ 4 ] -> [ 5 ] -> [ 1 ] -> None
    | 3 | => [ 5 ] -> [ 4 ] -> [ 1 ] -> None
    | 4 | => [ 5 ] -> [ 6 ] -> [ 2 ] -> [ 3 ] -> None
    | 5 | => [ 6 ] -> [ 4 ] -> [ 2 ] -> [ 3 ] -> None
    | 6 | => [ 5 ] -> [ 4 ] -> None

    Example Output:
    11
    9

    APPROACH:
    - Initial thoughts: I had no idea what to do

    - Plan: 
        - for each node, go to the neighbors
        - when at the neighbor, check if the node in the array of the neighbors
        - if so, increase the count
        - return the number of count divided by 2
    """
    count = 0

    for node in graph:
        for neigbor in graph[node]:
            if node in graph[neigbor]:
                count+=1

    return count // 2


graph = {
    0: [2, 5],
    2: [0, 3, 4],
    5: [0, 3, 6],
    3: [2, 5, 6],
    4: [2, 6],
    6: [5, 3, 7, 8, 4],
    7: [6, 8],
    8: [6, 7]
}

numBiDirectionalNodes = countBiDirectionalNodes(graph)
print("The number of bi-directional nodes is:", numBiDirectionalNodes)
