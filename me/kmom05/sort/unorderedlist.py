#!/usr/bin/python3
"""unorderedlist.py kmom05."""

from node import Node
from errors import ListIndexError, ListValueError


class UnorderedList:
    """Defina list class"""

    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def append(self, data):
        """Append new node in the list"""
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data, self.tail)
            self.tail = self.tail.next

        self._length += 1

    def set(self, index, data):
        """
        Replace value (data) for the node on the index place.
        If index is missing raise an exception
        """
        index = int(index)
        self[index] = data

    def size(self):
        """Return the size of the list."""
        return len(self)

    def get(self, index):
        """Return value of the node with the index."""
        index = int(index)
        return self[index]

    def index_of(self, data):
        """Show index of the data if data exists in the list."""
        ix = 0
        if len(self) == 0:
            raise ListValueError
        current_node = self.head
        if self.head.data != data:
            while current_node.next is not None and current_node.data != data:
                current_node = current_node.next
                ix += 1
        if current_node.data != data:
            raise ListValueError
        return ix

    def print_list(self):
        """Print all nodes in the list."""
        return self

    def get_node(self, data):
        """Get node from index."""
        if len(self) == 0:
            raise ListIndexError
        if self.head.data == data:
            return self.head
        current_node = self.head
        while current_node is not None and current_node.data != data:
            current_node = current_node.next
        if current_node is None:
            raise ListValueError
        return current_node

    def remove(self, data):
        """Remove the first node from the list which contains data."""
        try:
            to_be_removed = self.get_node(data)
        except ListIndexError as e:
            raise e
        if to_be_removed is self.head:
            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None
        elif to_be_removed is self.tail:
            if self.tail is not self.head:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            else:
                self.head = None
                self.tail = self.head
        else:
            to_be_removed.prev.next = to_be_removed.next
            to_be_removed.next.prev = to_be_removed.prev

        self._length -= 1

    def insertionsort(self):
        """Sort of unordered list (Insertion)."""
        for i in range(1, len(self)):
            j = i
            while j > 0:
                if isinstance(self[j-1], str) != isinstance(self[j], str):
                    if isinstance(self[j-1], str):
                        self[j], self[j-1] = self[j-1], self[j]
                    j -= 1
                elif self[j] < self[j-1]:
                    self[j], self[j-1] = self[j-1], self[j]
                    j -= 1
                else:
                    break
        return self

    def recursive_insertionsort(self, n=None):
        """Recursive sort of unordered list (Insertion)."""
        if n is None:
            n = len(self)
        if n <= 1:
            return None
        self.recursive_insertionsort(n - 1)
        last = self[n - 1]
        j = n - 2
        condition = True
        while j >= 0 and condition:
            if isinstance(self[j], str) != isinstance(last, str):
                if isinstance(self[j], str):
                    self[j + 1] = self[j]
                    j -= 1
            elif self[j] > last:
                self[j + 1] = self[j]
                j -= 1
            else:
                condition = False
        self[j + 1] = last
        return self

    def recursive_bubblesort(self, n=None):
        """Recursive sort of unordered list (Bubblesort)."""
        if n is None:
            n = len(self)
        if n == 1:
            return None
        for i in range(n - 1):
            if isinstance(self[i], str) != isinstance(self[i + 1], str):
                if isinstance(self[i], str):
                    self[i], self[i + 1] = self[i + 1], self[i]
            elif self[i] > self[i + 1]:
                self[i], self[i + 1] = self[i + 1], self[i]
        self.recursive_bubblesort(n - 1)
        return self

    def __len__(self):
        """Implement magic method __len__."""
        return self._length

    def __str__(self):
        """Implement magic method __len__."""
        current_node = self.head
        res = "None"
        if current_node is not None:
            res = []
            while current_node is not None:
                try:
                    data = str(current_node.data)
                except TypeError:
                    data = current_node.data
                res.append(data)
                current_node = current_node.next
            res = "[" + ", ".join(res) + "]"
        return res

    def __getitem__(self, index):
        """Implement magic method __getitem__."""
        if index < 0 or index > len(self) - 1:
            raise ListIndexError

        if index == 0:
            return self.head.data

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.data

    def __setitem__(self, index, value):
        """Implement magic method __setitem__."""
        if index < 0 or index > len(self) - 1 or (index == 0 and len(self) == 0):
            raise ListIndexError

        if index == 0:
            self.head.data = value

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        current_node.data = value
