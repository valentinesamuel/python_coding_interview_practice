from DS_Classes.TreeClass import TreeNode, BinarySearchTree

import sys
sys.path.append('../DS_Classes/')


def findKNodes(root: TreeNode, k: int | str):
    """
    PROBLEM: Implement a function findKNodes(root,k) which finds and returns nodes at k distance from the root in the given binary tree. An illustration is also provided for your understanding.

    Input: A binary search tree.

    Output: Returns all nodes in a list format which are at k distance from the root node

    Example Input:
    bst = {
    6 -> 4,9
    4 -> 2,5
    9 -> 8,12
    12 -> 10,14
    }
    where parent -> leftChild,rightChild
    k = 2


    Example Output:
    [2,5,8,12]

    APPROACH:
    - Initial thoughts: I was thinking of something like the find_tree_height but it didn't work out

    - Plan: 
        - create a tree array
        - traverse through the tree with a helper function that will populate the tree
        - return the tree

        - if the root is 0, we just return
        - if k is 0, we append to the tree because we just exhausted the distance for this traversal
        - else, we traverse the left and right with k-1 distance 
    """
    tree = []

    traverse(root, tree, k)

    return tree


def traverse(root: TreeNode, tree: BinarySearchTree, k: int | str):
    if root is 0:
        return
    if k == 0:
        tree.append(root.value)
    else:
        traverse(root.left, tree, k-1)
        traverse(root.right, tree, k-1)
