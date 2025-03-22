### BINARY TREE ###

# Binary trees are hierarchical data structures consisting of nodes with at most two children — commonly referred to as the left and right child.
# Unlike linked lists, which are linear and connect nodes sequentially, binary trees naturally represent hierarchical relationships.
# This allows for efficient searching, insertion, and deletion (especially when balanced).

# Advantages
# Hierarchical Structure: Ideal for representing hierarchical data (e.g., organizational charts, file systems).
# Efficient Operations: In a balanced binary search tree, search, insertion, and deletion can be performed in O(log n) time.
# Sorted Order Retrieval: An in-order traversal of a binary search tree yields the elements in sorted order.
# Dynamic Size: Like linked lists, binary trees grow dynamically without needing contiguous memory.

# Trade-Offs
# Unbalanced Trees: If not maintained properly, a binary tree can become skewed, degrading operations to O(n) in the worst case.
# Complex Implementation: Insertion, deletion, and balancing require more complex algorithms compared to linked lists or arrays.
# Memory Overhead: Each node stores extra pointers (for left and right children) compared to arrays.

# Comparison to Arrays and Linked Lists
# Arrays: Provide O(1) random access but are static in size and require contiguous memory.
# Linked Lists: Offer efficient O(1) insertions/deletions (given a pointer) but lack fast search capabilities.
# Binary Trees: When balanced, they provide a good compromise—efficient dynamic insertions/deletions and O(log n) search, though with added algorithmic complexity.
# Time Complexities (for a balanced binary search tree)
# Search: Average O(log n); worst-case O(n) if unbalanced.
# Insert: Average O(log n); worst-case O(n) if unbalanced.
# Delete: Average O(log n); worst-case O(n) if unbalanced.
# Traversal: O(n)

### Binary Tree Class Implementation ###

class BinaryTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def inorder_traversal(self) -> list:
        """Return the list of elements using in-order traversal."""
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []
        # Left subtree, current node, then right subtree
        return self._inorder(node.left) + [node.data] + self._inorder(node.right)

    def height(self) -> int:
        """Return the height of the tree."""
        return self._height(self.root)

    def _height(self, node) -> int:
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))