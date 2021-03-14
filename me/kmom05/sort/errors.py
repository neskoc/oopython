#!/usr/bin/python3
"""errors.py kmom04 (unordered list)"""

class ListIndexError(IndexError):
    """ Raised when peek or dequeue is used on an empty queue. """

class ListValueError(ValueError):
    """ Raised when peek or dequeue is used on an empty queue. """
