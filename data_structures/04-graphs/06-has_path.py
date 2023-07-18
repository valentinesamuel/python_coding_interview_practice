from DS_Classes.GraphClass import Graph
from DS_Classes.StackClass import MyStack as Stack
import sys
sys.path.append('../DS_Classes/')

def check_path(g:Graph, source, destination):
    """
    PROBLEM: You have to implement the check_path() function. It takes a source vertex and a destination vertex and tells us whether or not a path exists between the two.

    Input: A directed graph, a source value, and a destination value.

    Output: Returns True if a path exists from the source to the destination.

    Example Input:
    >>Adjacency List of Directed Graph<<
    | 0 | => [ 5 ] -> [ 2 ] -> None
    | 1 | => None
    | 2 | => [ 4 ] -> [ 3 ] -> None
    | 3 | => [ 6 ] -> None
    | 4 | => None
    | 5 | => [ 6 ] -> [ 3 ] -> None
    | 6 | => [ 4 ] -> [ 8 ] -> [ 7 ] -> None
    | 7 | => [ 8 ] -> None
    | 8 | => None
    >>Adjacency List of Directed Graph<<
    | 0 | => [ 1 ] -> None
    | 1 | => [ 3 ] -> [ 2 ] -> None
    | 2 | => [ 3 ] -> None
    | 3 | => None

    Example Output:
    >>True
    >>False

    APPROACH:
    - Initial thoughts: I had no idea what to do

    - Plan: 
        - perform a normal traversal, at each node, check if the node is the destination node
    """
    stack = Stack()
    stack.push(source)

    while not stack.is_empty():
        curr = stack.pop()
        if curr == destination:
            return True
        else:
            temp = g.array[curr].head_node  # Fix: Replaced "temp" with "curr"
            while temp:
                if temp.data == destination:
                    return True
                stack.push(temp.data)
                temp = temp.next_element

    return False