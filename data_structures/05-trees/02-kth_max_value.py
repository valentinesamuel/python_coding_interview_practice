def findKthMax(root, k):
    """
    PROBLEM: Implement a function findKthMax(root,k) which will take a BST and any number “k” as an input and return kth maximum number from that tree.

    Input: A binary search tree.

    Output: Returns kth maximum value from the given tree

    Example Input:
    bst = {
        6 -> 4,9
        4 -> 2,5
        9 -> 8,12
        12 -> 10,14
    }
    where parent -> leftChild,rightChild

    k = 3

    Example Output:
    10

    APPROACH:
    - Initial thoughts: I only knew that a tree could be represented in form of an array but i did not know more than that.

    - Plan: 
        - create a tree array
        - perform an inorder traversal to fill the array
        - if the length of the tree if less than k and k is less than 0, that means that k is out of bounds, if k is eithin pounds, we return value at the -kth index

        - for the inorder traversal,
            - if root is not None,
            - recursively perform the traversal on the left subtree and pass it the tree array that would come as a params.
            - if the tree is empty, append to the tree,
            - if the tree has elements and the last item in the tree is not the same as the current node's value, we append
            - we then perform an inorder traversal on the right subtree.
    """
    if root is None:
        return None
    tree = []

    inOrderTraversal(root, tree)

    if len(tree) > k > 0:
        return tree[-k]
    return None

def inOrderTraversal(root, tree):
    if root is not None:
        inOrderTraversal(root.left, tree)
        if len(tree) == 0:
            tree.append(root.val)
        if len(tree) > 0 and tree[-1] is not root.val:
            tree.append(root.val)
        inOrderTraversal(root.right, tree)

