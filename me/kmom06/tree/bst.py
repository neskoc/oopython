#!/usr/bin/python3
"""bst.py kmom06."""

from node import Node

class BinarySearchTree:
    """Defina bst class"""

    def __init__(self):
        self.root = None
        self._length = 0

    def insert(self, key, value):
        """Insert new node in the tree"""
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(key, value, self.root)
        self._length += 1

    @classmethod
    def _insert(cls, key, value, node):
        """Insert new node (class method)"""
        if node > key:
            if node.has_left_child():
                cls._insert(key, value, node.left)
            else:
                node.left = Node(key, value)
                node.left.parent = node
        elif node < key:
            if node.has_right_child():
                cls._insert(key, value, node.right)
            else:
                node.right = Node(key, value)
                node.right.parent = node
        else:
            node.value = value

    def inorder_traversal_print(self):
        """Print tree elements inorder"""
        node_list = []
        self.get_inorder_values(self.root, node_list)
        for node in node_list:
            print(node)

    @classmethod
    def get_inorder_values(cls, node, node_list):
        """Fetch bst elements inorder"""
        if node is not None:
            if node.has_left_child():
                cls.get_inorder_values(node.left, node_list)
            node_list.append(node.value)
            if node.has_right_child():
                cls.get_inorder_values(node.right, node_list)

    def get(self, key):
        """Return value of the node with the key."""
        node = self.find_node(self.root, key)
        # print("Node key:", node.key)
        return node.value

    def remove(self, key):
        """Remove the node with the key."""
        if key == 9:
            print(9)
        node = self.find_node(self.root, key)
        value = node.value

        if node.is_leaf():
            Node.remove_parents_link(node)
            if node == self.root:
                self.root = None
        elif not node.has_both_children():
            self.bypass(node)
        else:
            replacement_node = self.find_successor(node.right)
            if replacement_node.has_right_child():
                self.replace_parents_child(replacement_node, replacement_node.right)
            else:
                Node.remove_parents_link(replacement_node)
            node.key = replacement_node.key
            node.value = replacement_node.value
            replacement_node = None

        self._length -= 1
        return value

    def bypass(self, node):
        """Bypass node."""
        if node.has_left_child():
            self.replace_parents_child(node, node.left)
        else:
            self.replace_parents_child(node, node.right)

    def replace_parents_child(self, node, new_node):
        """Replace  parents child-node with a new node"""
        if node.parent is not None:
            if node.parent.left == node:
                node.parent.left = new_node
            else:
                node.parent.right = new_node
            new_node.parent = node.parent
            # node = new_node
        else:
            self.root = new_node
            self.root.parent = None

    def __len__(self)->int:
        """Implement magic method __len__."""
        return self._length

    def __getitem__(self, key)->Node:
        """Implement magic method __getitem__."""
        return self.find_node(self.root, key)

    def __setitem__(self, key, value):
        """Implement magic method __setitem__."""
        self.insert(key, value)

    def __contains__(self, key)->bool:
        """Implement magic method __conteins__ (in)."""
        try:
            self.find_node(self.root, key)
            return True
        except KeyError:
            return False

    def find_node(self, root_node, key):
        """Find node if exists."""
        if root_node is not None:
            if root_node.key == key:
                return root_node
            if root_node.key > key and root_node.has_left_child():
                return self.find_node(root_node.left, key)
            if root_node.key < key and root_node.has_right_child():
                return self.find_node(root_node.right, key)
        raise KeyError

    @classmethod
    def find_successor(cls, root_node):
        """Find left most node if exists."""
        if root_node is not None:
            if root_node.left is not None:
                return cls.find_successor(root_node.left)
            return root_node
        raise KeyError
