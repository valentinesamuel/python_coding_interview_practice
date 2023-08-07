from DS_Classes.TreeClass import TreeNode

import sys
sys.path.append('../DS_Classes/')


def findAncestors(root: TreeNode, k: int | str):
    """
    PROBLEM: Implement the findAncestors(root, k) function which will find the ancestors of the node whose value is “k”. Here root is the root node of a binary search tree and k is an integer value of node whose ancestors you need to find. An illustration is also given. Your code is evaluated on the tree given in the example.

    Input: A binary search tree.

    Output: Returns all the ancestors of k in the binary tree in a Python list.

    Example Input:
    bst = {
    6 -> 4,9
    4 -> 2,5
    9 -> 8,12
    12 -> 10,14
    }
    where parent -> leftChild,rightChild

    k = 10

    Example Output:
    [12,9,6]

    APPROACH:
    - Initial thoughts: I thought that if i could traverse to find a node, i can possibly, keep track of all the nodes that i have gone through

    - Plan: 
        - while there is still a node and the current node is not the child
            - if k > current.val
                - append current.val to an ancestors list and move the pointer right
            - if k < current.val
                - append current.val to an ancestors list and move the pointer left
        - return the reversed version of the ancestors list
    """
    if not root:
        return None
    ancestors = []
    current = root

    while current is not None:
        if k > current.val:
            ancestors.append(current.val)
            current = current.rightChild
        elif k < current.val:
            ancestors.append(current.val)
            current = current.leftChild
        else:
            return ancestors[::-1]
    return []
