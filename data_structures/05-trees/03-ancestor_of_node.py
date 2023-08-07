from DS_Classes.TreeClass import TreeNode

import sys
sys.path.append('../DS_Classes/')


def findAncestors(root: TreeNode, k: int | str):
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
