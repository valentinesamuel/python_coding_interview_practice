from DS_Classes.GraphClass import Graph
from DS_Classes.QueueClass import MyQueue as Queue
import sys
sys.path.append('../DS_Classes/')


def find_min(graph: Graph, source: int, destination: int):
    """
    PROBLEM: Implement the find_min() function which will take a directed graph and two vertices, A and B. The result will be the shortest path from A to B. Remember, the shortest path will contain the minimum number of edges.

    Input: A directed graph, a vertex A and a vertex B.

    Output: Returns number of edges in the shortest path between A and B.

    Example Input:
    >>Adjacency List of Directed Graph<<
    | 0 | => None
    | 1 | => [ 3 ] -> [ 2 ] -> None
    | 2 | => [ 5 ] -> [ 4 ] -> None
    | 3 | => None
    | 4 | => [ 5 ] -> None
    | 5 | => None

    Example Output:
    2

    APPROACH:
    - Initial thoughts: I thought about doing a normal traversal and keeping track of a minimum sum and running minimum sum

    - Plan: 
        - keeep track of the node's distance from the source node as well as an array of visited and non-visited nodes.
        - while the BFS is on going, if the node has not been visited,
            - add it to queue
            - mark it as visited,
            - set the distance to be the distance od the popped node + 1
            - if the node is the destination, return the distance array indexed at the destination
    """
    num_vertices = graph.vertices
    visited = [False] * graph.vertices
    distance = [0] * num_vertices
    queue = Queue()
    queue.enqueue(source)
    visited[source] = True

    while not queue.is_empty():
        curr_node = queue.dequeue()
        temp = graph.array[curr_node].head_node
        while temp:
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                visited[temp.data] = True
                distance[temp.data] = distance[curr_node] + 1
                if temp is destination:
                    return distance[destination]
            temp = temp.next_element

    return -1

