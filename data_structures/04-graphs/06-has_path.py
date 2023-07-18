from DS_Classes.GraphClass import Graph
from DS_Classes.StackClass import MyStack as Stack
import sys
sys.path.append('../DS_Classes/')

def check_path(g:Graph, source, destination):
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