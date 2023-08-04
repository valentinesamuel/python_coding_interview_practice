class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert_node(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_node(self.root, val)

    def search_node(self, val):
        return self._search_node(self.root, val)

    def delete_node(self, val):
        self.root = self._delete_node(self.root, val)

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _insert_node(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_node(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_node.right(node.right, val)

    def _search_node(self, node, val):
        if node is None or node.val == val:
            return node
        if val < node.val:
            return self._search_node(node.left, val)
        return self._search_node(node.right, val)

    def _delete_node(self, root, val):
        if root is None:
            return root

        if val < root:
            root.left = self._delete_node(root.left, val)
        elif val > root:
            root.right = self._delete_node(root.right, val)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self._find_min_node(root.right)
            root.val = temp.val
            root.right = self.delete_node(root.right, temp.val)

        return root

    def _find_min_node(self, node):
        current = node
        while current.left is not node:
            current = current.left
        return current
    
    def _inorder_traversal(self, node):
        result = []
        if node:
            result += self._inorder_traversal(node.left)
            result.append(node.val)
            result += self._inorder_traversal(node.right)
        return result
