from DS_Classes.TreeClass import TreeNode

import sys
sys.path.append('../DS_Classes/')


def findMin(root: TreeNode):
    """
    PROBLEM: Implement the findMin(root) function which will find the minimum value in a given Binary Search Tree. Remember, a Binary Search Tree is a Binary Tree which satisfies the following property. An illustration is also provided to jog your memory.

    Input: A binary search tree.

    Output: Returns minimum integer value from a given binary search tree
    Example Input:
    bst = {
    6 -> 4,9
    4 -> 2,5
    9 -> 8,12
    12 -> 10,14
    }
    where parent -> leftChild,rightChild

    Example Output:
    2

    APPROACH:
    - Initial thoughts: I figured that no need to do a bfs or dfs since all the nodes in the subtree of the current node is less than the node, that means we would always traverse left

    - Plan: 
        - while there is still a left child,
        - move to the left
        - return the value at the end
    """
    
    if (root is None):
        return None
    while root.left:
        root = root.left
    return root.value
