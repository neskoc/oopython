"""
Node class for trie datastructure.

@author: Nenad Cuturic
"""

class Node:
    """
    Node class
    """
    def __init__(self, value=None, freq=None, stop=None):
        self.value = value
        self._freq = freq
        self.stop = stop
        self.children = {}

    def __iter__(self):
        # Loop all children nodes
        for key in self.children:
            yield key

    @property
    def freq(self) -> float:
        """Get Node _freq."""
        return self._freq

    @freq.setter
    def freq(self, freq):
        """Set Node _freq."""
        if freq >= 0:
            self._freq = freq
        else:
            raise ValueError("Frequency is not allowed to be less then zero")

    @freq.getter
    def freq(self):
        """Get Node _freq."""
        return self._freq

    def __get__(self, obj, objtype=None):
        return self.value

    def __contains__(self, letter)->bool:
        """Implement magic method __conteins__."""
        return letter in self.children.keys()

    def __setitem__(self, letter, node):
        self.children[letter] = node

    def __getitem__(self, letter):
        return self.children[letter]

    def has_children(self):
        """Check if node has children

        Returns:
            [bool]: True if it has
        """
        return bool(len(self.children.items()))
