#!/usr/bin/python3
"""node.py kmom05 (list)"""

class Node:
    """
    Node class
    """

    def __init__(self, data, prev_=None, next_=None):
        """
        Initialize object with the data and set next/prev to None.
        next will be assigned later when new data needs to be added.
        """

        self.data = data
        self.prev = prev_
        self.next = next_
