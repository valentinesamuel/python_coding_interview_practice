from DS_Classes.TreeClass import BinarySearchTree, TreeNode

import sys
sys.path.append('../DS_Classes/')


def findMin(root: TreeNode):

    
    if (root is None):
        return None
    while root.left:
        root = root.left
    return root.value
