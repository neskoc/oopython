#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nenad Cuturic
"""

from trie import SearchMiss, Trie
import treevizer

class SpellChecker:
    """
    SpellChecker class
    """

    def __init__(self, l_filename='test_dict.txt'):
        self.trie = Trie()
        self._filename = l_filename
        self._generate_trie()
        self.test_list = ["a", "d", "b", "e", "c"]
        self.counter = 0

    @staticmethod
    def _print_menu():
        """
        Show menu
        """
        print("""
        1) Check a word
        2) Get word suggestions
        3) Change dictionary
        4) Print all words
        5) Remove a word
        q) quit.
        """)
        inp = input("Choice: ")
        return inp

    def _process_choice(self, inp):
        """
        Make a choice.

        Parameters
        ----------
        inp : str
            Choice value and optional filename

        Returns
        -------
        str | bool
            Return new filename if changed, True if quit and otherwise False.

        """
        if inp == '1':
            self.check_word()
        elif inp == '2':
            self.get_word_suggestions()
        elif inp == '3':
            self.change_dictionary()
        elif inp == '4':
            self.print_trie()
        elif inp == '5':
            self.remove_word()
        elif inp in ('q', 'quit'):
            return True
        else:
            print('Nonexistent choice! Please try again.')
        return False

    def main(self):
        """
        Do main loop.

        Returns
        -------
        None.

        """
        finished = False
        while not finished:
            inp = self._print_menu()
            finished = self._process_choice(inp)
        print('Have a nice day!')

    def _generate_trie(self):
        """
        Generate trie from word list in self._filename
        """
        res = self.trie.generate_trie(self._filename)
        print(res)
        return False

    def change_dictionary(self):
        """
        Replace old dictionary with the new one from file
        """
        inp = input("Filename: ")
        self.trie = Trie()
        self._filename = inp
        self._generate_trie()
        return False

    def check_word(self):
        """
        Check whether word exists in trie data structure
        """
        inp = input("Word: ")
        try:
            if inp in self.trie:
                print(f'Word "{inp}" with frequency {self.trie.freq} is found')
        except SearchMiss as err:
            print(err.message)
        return False

    def remove_word(self):
        """
        Remove word from trie data structure
        """
        inp = input("Word: ")
        try:
            del self.trie[inp]
            print(f"Word '{inp}' removed from the trie")
            treevizer.to_png(sc.trie.root, structure_type="trie",
                             dot_path="trie_after_remove.dot",
                             png_path=f"{self._filename}{self.counter}_after_remove_{inp}.png")
            self.counter += 1
        except SearchMiss as err:
            print(err.message)
        return False

    def print_trie(self):
        """
        Print whole dictionary
        """
        self.trie.print_all_words()
        return False

    def get_word_suggestions(self):
        """
        Get word suggestions
        """
        prefix = input("Prefix: ")
        while True:
            if len(prefix.split()) != 1:
                return False
            try:
                node = self.trie.find_node(prefix)
            except SearchMiss:
                pass
            if 'node' in locals():
                suffixes = self.trie.find_all_words(node)
                suggestions = sorted(suffixes.items(), key=lambda x: x[1])
                nr_of_iterations = len(suggestions)
                if nr_of_iterations > 10:
                    nr_of_iterations = 10
                for index in range(nr_of_iterations):
                    print(f"{prefix}{suggestions[index][0]}({suggestions[index][1]})")
            print(" *** Quit by typing space any word after! ***")
            prefix += input(f" Prefix: {prefix}")
        return False


if __name__ == "__main__":
    # filename = 'tiny_frequency.txt'
    # filename = 'frequency.txt'
    filename = 'test_dict.txt'
    # filename = 'frequency400.txt'
    sc = SpellChecker(filename)
    treevizer.to_png(sc.trie.root, structure_type="trie",
                     dot_path="trie.dot", png_path=f"{filename}.png")
    # breakpoint()
    sc.main()
