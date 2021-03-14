"""
Trie datastructure for storing dictionary with words and its frequencies.

@author: Nenad Cuturic
"""

from node import Node

class Trie:
    """
    Trie class
    """

    def __init__(self, filename=None):
        self.root = Node()
        self.freq = None
        if filename is not None:
            self.generate_trie(filename)

    def generate_trie(self, filename):
        """
        Generate trie datastructure from word list in filename
        """
        self.root = Node()
        count = 0
        with open(filename, 'r') as fp:
            for line in fp:
                count += 1
                split_line = line.split()
                if len(split_line) == 1:
                    freq = 0
                elif len(split_line) == 2:
                    freq = split_line[1]
                else:
                    print("Wrong format of the line in the file", line)
                    return False
                self.insert(split_line[0], freq)
            return f"{count} words added to the trie"

    def __getitem__(self, key)->Node:
        """Implement magic method __getitem__."""
        return self.find_node(key)

    @staticmethod
    def _insert(node, letter, freq=None, stop=False):
        """Insert letter in node"""
        if letter in node:
            if stop:
                node[letter].freq = freq
                node[letter].stop = stop
            return node[letter]
        node[letter] = Node(letter, freq, stop)
        return node[letter]

    def insert(self, word, freq):
        """Insert word in trie"""
        next_node = self.root
        word_as_list = list(word)
        for letter in word_as_list[:-1]:
            next_node = self._insert(next_node, letter)
        self._insert(next_node, word_as_list[-1], float(freq), True)

    def __contains__(self, word)->bool:
        """Implement magic method __conteins__ (word)."""
        next_node = self.root
        word_as_list = list(word)
        for letter in word_as_list:
            if letter in next_node:
                next_node = next_node[letter]
            else:
                raise SearchMiss(word)
        if next_node.stop:
            self.freq = next_node.freq
            return True
        raise SearchMiss(word)

    def find_node(self, word)->Node:
        """Find node matching word."""
        next_node = self.root
        word_as_list = list(word)
        for letter in word_as_list:
            if letter in next_node:
                next_node = next_node[letter]
            else:
                raise SearchMiss(word)
        return next_node

    def remove_node(self, rem_list):
        """Remove node

        Args:
            rem_list (list<dict>): [description]
        """
        if rem_list[-1]["node"].has_children():
            return
        rem_list[-2]["node"].children.pop(rem_list[-1]["char"], None)
        del rem_list[-1]
        if len(rem_list) > 1:
            self.remove_node(rem_list)

    def __delitem__(self, word)->bool:
        """Implement magic method __del__ (word)."""
        if self.find_node(word):
            word_as_list = list(word)
            node_list = []
            next_node = self.root
            node_list.append(
                {
                    "char": None,
                    "node": next_node
                })
            for letter in word_as_list:
                next_node = next_node[letter]
                node_list.append(
                    {
                        "char": letter,
                        "node": next_node
                    })
            if node_list[-1]["node"].has_children():
                node_list[-1]["node"].stop = False
                node_list[-1]["node"].freq = 0
            else:
                node_list[-2]["node"].children.pop(node_list[-1]["char"], None)
            del node_list[-1]
            self.remove_node(node_list)

    def get_sorted_words(self):
        """
        Help getting all sorted words from trie
        """
        word_list_with_freq = self.find_all_words()
        word_list = list(word_list_with_freq.keys())
        return self.merge_sort(word_list, high=len(word_list)-1)

    def print_all_words(self):
        """
        Print all words from trie sorted by the words
        """
        word_list_with_freq = self.find_all_words()
        word_list = list(word_list_with_freq.keys())
        sorted_word_list = self.merge_sort(word_list, high=len(word_list)-1)
        for word in sorted_word_list:
            print(f"{word}: {word_list_with_freq[word]}")
        print("Number of printed words:", len(word_list_with_freq))

    def find_all_words(self, node=None)->list:
        """
        Find all words in the trie and return list
        """
        word = ''
        if node is None:
            node = self.root
        word_dict = {}
        res = {}
        if node.has_children():
            res = self.get_words(word_dict, node, node, word)
        return res

    def get_words(self, word_dict, start_node, node, word):
        """Traverse through trie and get words

        Args:
            word_dict (dict): Dict for saving of found words
            node (Node): Start node from trie
            word (str): Keeps track of the traversed letters

        Returns:
            dict: Dictionary with words as keys and frequencies as values
        """
        for key in node:
            lword = word + key
            if node[key].has_children():
                self.get_words(word_dict, start_node, node[key], lword)
            if node[key].stop:
                word_dict[lword] = node[key].freq
        if node == start_node:
            return word_dict
        return None

    @classmethod
    def merge_lists(cls, word_list, low, mid, high):
        """Merge sort

        Args:
            word_list ([type]): [description]
            low ([type]): [description]
            mid ([type]): [description]
            high ([type]): [description]

        Returns:
            [type]: [description]
        """
        help_list = []
        left = low
        right = mid + 1
        while left <= mid and right <= high:
            if word_list[left] <= word_list[right]:
                help_list.append(word_list[left])
                left += 1
            else:
                help_list.append(word_list[right])
                right += 1
        while left <= mid:
            help_list.append(word_list[left])
            left += 1
        while right <= high:
            help_list.append(word_list[right])
            right += 1
        for k in range(high - low + 1):
            word_list[low + k] = help_list[k]
        return word_list

    @classmethod
    def merge_sort(cls, word_list, low=0, high=0)->list:
        """Sort word list using merge sort algorithm

        Args:
            word_list ([list<str>]): Word list to be sorted
            low (int): lower bound
            high (int): higher bound

        Returns:
            list: Sorted list of words
        """
        if low < high:
            mid = (low + high) // 2
            cls.merge_sort(word_list, low, mid)
            cls.merge_sort(word_list, mid + 1, high)
            word_list = Trie.merge_lists(word_list, low, mid, high)
        return word_list


class SearchMiss(Exception):
    """Base class for SearchMiss exceptions

    Attributes:
        word -- word which caused the error
        message -- explanation of the error
    """

    def __init__(self, word, message="The searched word couldn't be found"):
        self.word = word
        self.message = f"{message}: '{word}'"
        super().__init__(self.message)
