from DS_Classes.GraphClass import Graph
from DS_Classes.StackClass import MyStack as Stack
import sys
sys.path.append('../DS_Classes/')

def detect_cycle(g: Graph) -> bool:
    """
    PROBLEM: The concept of loops or cycles is very common in graph theory. A cycle exists when you traverse the directed graph and come upon a vertex that has already been visited.You have to implement the detect_cycle function which tells you whether or not a graph contains a cycle.

    Input: A directed graph.

    Output: True if a cycle exists. False if it doesn’t.

    Example Input:
    >>Adjacency List of Directed Graph<<
    | 0 | => [ 1 ] -> None
    | 1 | => [ 3 ] -> [ 2 ] -> None
    | 2 | => None
    | 3 | => [ 0 ] -> None
    >>Adjacency List of Directed Graph<<
    | 0 | => [ 1 ] -> None
    | 1 | => [ 2 ] -> None
    | 2 | => None

    Example Output:
    True
    False

    APPROACH:
    - Initial thoughts: I had no idea what to do

    - Plan: 
        - since we were not given a source node, we have to go through every element of the list
        - for evenry head of linked list in the graph array,
            - if it is not an empty linked list, add it has not been visited, ass it to stack, and traverse through the remaining nerighbours.


    Note: this implementation does not work vwry weel because of the nature of input. But the concept remains clear
    """
    visited = set()
    stack = Stack()

    for node in g.array:
        if node and node.get_head():
            stack.push(node.get_head().data)

            while not stack.is_empty():
                current_node = stack.pop()
                if current_node in visited:
                    return True
                visited.add(current_node)
                temp = node.get_head().next_element
                while temp:
                    if temp.data not in visited:
                        stack.push(temp.data)
                    temp = temp.next_element
    return False
