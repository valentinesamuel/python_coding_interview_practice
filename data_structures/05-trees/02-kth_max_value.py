def findKthMax(root, k):
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

