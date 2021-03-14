#!/usr/bin/python3
"""errors.py kmom04"""

class EmptyQueueException(Exception):
    """ Raised when peek or dequeue is used on an empty queue. """
