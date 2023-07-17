from DS_Classes.GraphClass import Graph
from DS_Classes.StackClass import MyStack as Stack
import sys
sys.path.append('../DS_Classes/')


def dfs_traversal(g: Graph, source: int | str) -> str:
    
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
