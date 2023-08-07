def findHeight(root):
    if root is None:
        return -1
    else:
        return 1 + max(findHeight(root.leftChild), findHeight(root.rightChild))