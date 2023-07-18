from DS_Classes.GraphClass import Graph
import sys
sys.path.append('../DS_Classes/')

def DFS(graph:Graph, current_node, visited):
    visited.append(current_node)

    for neighbour in graph[current_node]:
        if not neighbour in visited:
            DFS(graph, neighbour, visited)


def find_mother_vertex(g):
    """
    PROBLEM: You have to implement the find_mother_vertex() function which will take a directed graph as an input and find out which vertex is the mother vertex in the graph. By definition, the mother vertex is a vertex in a graph such that all other vertices in a graph can be reached by following a path from that vertex. A graph can have multiple mother vertices, but you only need to find one.

    Input: A directed graph.

    Output: Returns the value of the mother vertex if it exists. Otherwise, it returns -1

    Example Input:
    0: [1, 2],
    1: [3],
    2: [],
    3: []

    Example Output:
    0

    APPROACH:
    - Initial thoughts: I had no idea what to do

    - Plan: 
        - using the explanation below. it works on Kosaraju's Strongly Connected Components Algorithm.
        - for every node in the graph, run a DFS on all of them recursively, then after the DFS, the last node to be returned from the stack will be the mother node


    Note: this implementation does not work vwry weel because of the nature of input. But the concept remains clear
    """
    mother_node = 0
    visited = []

    for node in range(len(g)):
        if not node in visited:
            DFS(g, node, visited)
            mother_node = node

    return mother_node


graph = {
    0: [1, 2],
    1: [3],
    2: [],
    3: []
}
mother = find_mother_vertex(graph)
print("The mother node is:", mother)

"""
Okay, let's imagine we have a group of people, and each person is connected to some other people in the group. We can think of this group as a graph, where each person is a node, and the connections between them are the edges of the graph.

Now, let's say there is one special person in the group who is connected to every other person directly or indirectly. We call this person the "mother node" because she is like the mother of the entire group.

To find the mother node efficiently, we can use a simple algorithm called "Depth-First Search" or DFS. Here's how it works:

- We start by picking any person in the group.
- We visit that person and mark them as "visited."
- Then, we go to one of the people they are connected to (a neighbor) who hasn't been visited yet.
- We repeat steps 2 and 3 for this new person, marking them as visited and visiting one of their unvisited neighbors.
- We keep doing this until we reach a person who has no unvisited neighbors.
- At this point, we backtrack to the previous person we visited and continue exploring their unvisited neighbors.
- We repeat steps 2 to 6 until we have visited all the people in the group.
- The last person we visited in this process is our potential mother node because if there was a mother node, she would be connected to everyone, and hence there would be no unvisited neighbors left.

Let me explain this algorithm using a simple example with a group of people:

Suppose we have five people (nodes) named A, B, C, D, and E. Let's say the connections between them are as follows:
A -> B, C
B -> C, D
C -> D
D -> E

To find the mother node, we can start with person A and apply the DFS algorithm:

Start with person A.
Mark A as visited.
Visit B (an unvisited neighbor of A) and mark it as visited.
Visit C (an unvisited neighbor of B) and mark it as visited.
Visit D (an unvisited neighbor of C) and mark it as visited.
Visit E (an unvisited neighbor of D) and mark it as visited.
Since E has no unvisited neighbors, we backtrack to D.
Since D has no unvisited neighbors, we backtrack to C.
Since C has no unvisited neighbors, we backtrack to B.
Since B has no unvisited neighbors, we backtrack to A.
At this point, we have visited all the people, and the last person we visited is E. So, in this example, E is the mother node because she is connected to everyone directly or indirectly.
"""