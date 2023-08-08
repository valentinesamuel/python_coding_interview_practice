from DS_Classes.TreeClass import TreeNode, BinarySearchTree

import sys
sys.path.append('../DS_Classes/')


def findKNodes(root: TreeNode, k: int | str):
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
