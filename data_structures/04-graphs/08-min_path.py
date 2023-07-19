from DS_Classes.GraphClass import Graph
from DS_Classes.QueueClass import MyQueue as Queue
import sys
sys.path.append('../DS_Classes/')


def find_min(graph: Graph, source: int, destination: int):
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

