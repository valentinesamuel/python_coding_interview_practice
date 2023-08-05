from DS_Classes.GraphClass import Graph
from DS_Classes.QueueClass import MyQueue as Queue
import sys
sys.path.append('../DS_Classes/')


def bfs_traversal(g: Graph, source):
    """
    PROBLEM: You have to implement the Breadth First Search traversal in Python. We have already covered the logic behind this algorithm. All that's left to do is to flesh it out in code.

    Note: Your solution should work for both connected and unconnected graphs.

    Input: A directed graph in the form of an adjacency list and an integer indicating the starting vertex number (source).

    Output: A string containing the vertices of the graph listed in the correct order of traversal.

    Example Input:
    Source: 0 
    >>Adjacency List of Directed Graph<<
    | 0 | => [ 2 ] -> [ 1 ] -> None
    | 1 | => [ 4 ] -> [ 3 ] -> None
    | 2 | => None
    | 3 | => None
    | 4 | => None

    Example Output:
    02143 or 02134 or 01234 or 01243

    APPROACH:
    - Initial thoughts: I had no idea what to do

    - Plan: 
        - enqueue the source vertex
        - while the queue is not empty
            - dequeue
            - add the dequeued to the result
            - starting from the graph array at the index of the dequeued
            - get the head node
            - traverse to the end of the linked list while enqueuing the node's data
    """
    result = ""
    num_of_vertices = g.vertices

    queue = Queue()
    queue.enqueue(source)

    while not queue.is_empty():
        curr = queue.dequeue()
        result = result + str(curr)
        head_node = g.array[curr].get_head()

        while head_node:
            queue.enqueue(head_node.data)
            head_node = head_node.next_element

    return result
