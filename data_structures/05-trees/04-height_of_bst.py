def findHeight(root):
    """
    PROBLEM: Implement a function findHeight(root) which returns the height of a given binary search tree. An illustration is also provided for your understanding.

    Input: A binary search tree.

    Output: Returns the maximum depth or height of a binary tree

    Example Input:
    bst = {
    6 -> 4,9
    4 -> 2,5
    9 -> 8,12
    12 -> 10,14
    }
    where parent -> leftChild,rightChild


    Example Output:
    3

    APPROACH:
    - Initial thoughts: I was thinking of something like using recursion to solve for it like in the fibonacci numbers but i could not quite place it properly.

    - Plan: 
        - if root is None, return -1
        - else return 1 + the max between the height of the left and rith sub tree
    """
    if root is None:
        return -1
    else:
        return 1 + max(findHeight(root.leftChild), findHeight(root.rightChild))