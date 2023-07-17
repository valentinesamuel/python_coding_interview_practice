from DS_Classes.GraphClass import Graph
from DS_Classes.StackClass import MyStack as Stack
import sys
sys.path.append('../DS_Classes/')


def dfs_traversal(g: Graph, source: int | str) -> str:
    """
    PROBLEM: You have to implement the Depth First Search algorithm on a directed graph using the data structures which we have implemented in the previous sections.
    
    Note: Your solution should work for both connected and unconnected graphs.

    Input: A directed graph in the form of an adjacency list and a starting vertex.

    Output: A string containing the vertices of the graph listed in the correct order of traversal.

    Example Input:
    Source: 0 
    >>Adjacency List of Directed Graph<<
    | 0 | => None
    | 1 | => [ 3 ] -> [ 2 ] -> None
    | 2 | => [ 5 ] -> [ 4 ] -> None
    | 3 | => [ 6 ] -> None
    | 4 | => None
    | 5 | => None
    | 6 | => None

    Example Output:
    124536 or 136254

    APPROACH:
    - Initial thoughts: I had no idea what to do

    - Plan: 
        - push the source vertex to stack
        - while the stack is not empty
            - pop stack
            - add the poped element to the result
            - starting from the graph array at the index of the popped element
            - get the head node
            - traverse to the end of the linked list while pushing the  node's data to the stack
    """
    result = ""
    stack = Stack()
    stack.push(source)
    visited = set()

    while not stack.is_empty():
        curr = stack.pop()
        result += str(curr)
        visited.add(curr)

        head = g.array[curr].get_head()
        while head:
            stack.push(head.data)
            head = head.next_element

    return result
