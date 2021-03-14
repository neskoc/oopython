#!/usr/bin/python3
"""node.py kmom06 (bst)"""

class Node:
    """
    Node class
    """

    def __init__(self, key, value, parent=None):
        """Initialize node with the key/value and set parent to None."""
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def has_left_child(self)->bool:
        """Check if node has a left child."""
        return self.left is not None

    def has_right_child(self)->bool:
        """Check if node has a right child."""
        return self.right is not None

    def has_both_children(self)->bool:
        """Check if node has both left and right child."""
        return self.left is not None and self.right is not None

    def has_parent(self)->bool:
        """Check if node has a parent."""
        return self.parent is not None

    def is_left_child(self)->bool:
        """Check if node is a left child."""
        if self.parent is not None:
            if self.parent.left == self:
                return True
        return False

    def is_right_child(self)->bool:
        """Check if node is a right child."""
        if self.parent is not None:
            if self.parent.right == self:
                return True
        return False

    def is_leaf(self)->bool:
        """Check if node is a leaf (no children)."""
        return not self.has_right_child() and not self.has_left_child()

    def __lt__(self, other)->bool:
        """Implement magic method __lt__."""
        if isinstance(other, Node):
            return self.key < other.key
        return self.key < other

    def __gt__(self, other)->bool:
        """Implement magic method __gt__."""
        if isinstance(other, Node):
            return self.key > other.key
        return self.key > other

    def __eq__(self, other)->bool:
        """Implement magic method __eq__."""
        if isinstance(other, Node):
            return self.key == other.key
        return self.key == other

    def __str__(self):
        """Implement magic method __str__."""
        return f"({self.key}:{self.value})"

    @classmethod
    def remove_parents_link(cls, node):
        """Remove parents link to the node."""
        if node.parent is not None:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
