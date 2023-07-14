from DS_Classes.GraphClass import Graph
from DS_Classes.QueueClass import MyQueue as Queue
import sys
sys.path.append('../DS_Classes/')


def bfs_traversal(g: Graph, source):
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
