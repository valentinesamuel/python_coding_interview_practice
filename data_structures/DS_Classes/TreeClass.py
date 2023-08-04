class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_node(self, val):
        """insert a node into the bst:\n
        If the tree is empty, make the node become
        the root else, insert into in the tree

        Args:
            val (str|int): integer or string
        """
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_node(self.root, val)

    def search_node(self, val):
        """search for a node in the bst:\n        
        call the internal search method

        Args:
            val (str|int): integer or string
        """
        return self._search_node(self.root, val)

    def delete_node(self, val):
        """delete a node in the bst:\n        
        Call the internal delete method

        Args:
            val (str|int): integer or string
        """
        self.root = self._delete_node(self.root, val)

    def inorder_traversal(self):
        """Perform and inorder of the bst:\n
        Call the internal inorder traversal method

        Args:
            val (str|int): integer or string
        """
        return self._inorder_traversal(self.root)

    def _insert_node(self, root, val):
        """
        If val is smaller than the root and the left subtree is empty, we make the new the node the \nroot of the left subtree, else we recursively call the insert function untill we reach a leaf node. Same thing goes for the right subtree.
        """
        if val < root.val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self._insert_node(root.left, val)
        else:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self._insert_node.right(root.right, val)

    def _search_node(self, root, val):
        """
        If val is smaller than the node of this subtree, we search the left subtree, else we search the right subtree
        """
        if root is None or root.val == val:
            return root
        if val < root.val:
            return self._search_node(root.left, val)
        return self._search_node(root.right, val)

    def _delete_node(self, root, val):
        """
        If the tree is empty, we return None
        """
        if root is None:
            return root

        """
        If the tree is not empty, we traverse through the tree until we get to the node we want to delete where we have to check if there is one, two or no subtrees.
        """
        if val < root:
            # we go to the left subtree
            root.left = self._delete_node(root.left, val)
        elif val > root:
            # we go to the right subtree
            root.right = self._delete_node(root.right, val)
        else:
            """now we have gotten to the node, we need to check if therer is a left, right or no subtrees at all"""
            if root.left is None:
                # if there is no left subtree, store a reference to the right subtree and remove the node from the tree and return the right child so that it links up with the parent
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                # if there is no right subtree, store a reference to the left subtree and remove the node from the tree and return the left child so that it links up with the parent
                temp = root.left
                root = None
                return temp

            """if there is no no subtree, find the smallest node in the right subtree (successor), swap the root to be the successor and then, starting from the right subtree, look for the node to be delete which will now be a leaf node"""
            temp = self._find_min_node(root.right)
            root.val = temp.val
            root.right = self.delete_node(root.right, temp.val)

        return root

    def _find_min_node(self, root):
        """Since the minimum of any subtree will always be the left most node of the left subtree, we keep on traversing to the left"""
        current = root
        while current.left is not root:
            current = current.left
        return current

    def _inorder_traversal(self, root):
        """
        we first visit the left subtree, then we visit the root and then the right subtree
        """
        result = []
        if root:
            result += self._inorder_traversal(root.left)
            result.append(root.val)
            result += self._inorder_traversal(root.right)
        return result
