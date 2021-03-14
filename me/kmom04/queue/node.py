#!/usr/bin/python3
"""node.py kmom04"""

class Node:
    """
    Node class
    """

    def __init__(self, data, next_=None):
        """
        Initialize object with the data and set next to None.
        next will be assigned later when new data needs to be added.
        """

        self.data = data
        self.next = next_
