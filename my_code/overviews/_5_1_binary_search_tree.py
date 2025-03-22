from _5_0_binary_tree import BinaryTree

### Binary Tree Class Implementation ###

class BinarySearchTree(BinaryTree):

    def insert(self, data: int):
        """Insert data into the BST while maintaining its ordered property."""
        if self.root is None:
            self.root = self.Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data: int):
        if data <= node.data:
            if node.left is None:
                node.left = self.Node(data)
            else:
                self._insert(node.left, data)
        else:  # data > node.data
            if node.right is None:
                node.right = self.Node(data)
            else:
                self._insert(node.right, data)

    def search(self, data: int) -> bool:
        """Return True if data is found in the BST, False otherwise."""
        return self._search(self.root, data)

    def _search(self, node, data: int) -> bool:
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)
        
    def __contains__(self, data: int) -> bool:
        """Enable the use of 'in' keyword for checking if data is in the BST."""
        return self.search(data)


# Example usage:
if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [7, 3, 9, 2, 5, 8, 10]
    for v in values:
        bst.insert(v)
    
    # Using the __contains__ method via 'in'
    print("In-order Traversal (sorted):", bst.inorder_traversal())
    print("Does the tree contain 5?", 5 in bst)    # Expected: True
    print("Does the tree contain 11?", 11 in bst)  # Expected: False
    print("Tree Height:", bst.height())