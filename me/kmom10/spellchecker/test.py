#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unittest trie datastructure.

@author: Nenad Cuturic
"""
import unittest
from trie import Trie, SearchMiss

class TestFunc(unittest.TestCase):
    """
    Main test function
    """

    def setUp(self):
        """ Setup each test. """
        self.trie = Trie('test_dict.txt')

    def test_generate_dict(self):
        """Test remove."""
        filename = 'test_dict.txt'
        self.trie.generate_trie(filename)
        root_keys = ['h', 't', 'g', 'R', 'V']
        for key in root_keys:
            self.assertIn(key, self.trie.root.children.keys())
        test_words = ['the', 'Roy', 'hoard']
        for word in test_words:
            next_node = self.trie.root
            word_as_list = list(word)
            for letter in word_as_list:
                self.assertIn(letter, next_node.children.keys())
                next_node = next_node.children[letter]
            self.assertTrue(next_node.stop)

    def test_searchmiss_exception(self):
        """Test invalid search and remove."""
        with self.assertRaises(SearchMiss):
            self.trie.find_node('missing')
        with self.assertRaises(SearchMiss):
            del self.trie['missing']

    def test_search(self):
        """Test search."""
        test_words = ['the', 'Roy', 'hoard']
        for word in test_words:
            self.assertIn(word, self.trie)

    def test_remove_word(self):
        """Remove independent word (independent leaf)."""
        self.assertIn('R', self.trie.root.children.keys())
        del self.trie['Roy']
        with self.assertRaises(KeyError):
            print(self.trie.root.children['R'])
        # remove in the middle (only stop should be changed to False)
        e_node = self.trie.root.children['t'].children['h'].children['e']
        self.assertTrue(e_node.stop)
        del self.trie['the']
        self.assertFalse(e_node.stop)
        # remove haft-leaf half in th middle
        h_node = self.trie.root.children['h']
        o_node = h_node.children['o']
        a_node = o_node.children['a']
        r_node = a_node.children['r']
        d_node = r_node.children['d']
        self.assertTrue(d_node.stop)
        del self.trie['hoard']
        with self.assertRaises(KeyError):
            o_node = h_node.children['o']

    def test_change_dict(self):
        """Test replacing the dictionary."""
        # prior
        with self.assertRaises(SearchMiss):
            self.trie.find_node('possible')
        self.assertIn('adcd', self.trie)
        # posterior
        filename = 'tiny_frequency.txt'
        self.trie.generate_trie(filename)
        with self.assertRaises(SearchMiss):
            print(self.trie.find_node('adcd'))
        self.assertIn('possible', self.trie)

    def test_merge_sort(self):
        """Test merge sort on the unordered word list."""
        # test empty
        self.assertEqual('', Trie.merge_sort('', high=0))
        # test one word
        self.assertEqual('ett', Trie.merge_sort('ett', high=0))
        #test two words
        word_list = ['two', 'one']
        merge_sorted_list = Trie.merge_sort(word_list, high=len(word_list)-1)
        word_list.sort()
        self.assertEqual(word_list, merge_sorted_list)
        # test larger list
        filename = 'test_dict.txt'
        word_list = get_test_list_from_file(filename)
        merge_sorted_list = Trie.merge_sort(word_list, high=len(word_list)-1)
        self.assertEqual(word_list, merge_sorted_list)

    def tearDown(self):
        """ teardown test """
        self.trie = None


def get_test_list_from_file(filename):
    """Generate list from file (one word in the beginning av separate lines)."""
    word_list = []
    with open(filename, 'r') as fp:
        for line in fp:
            split_line = line.split()
            if len(split_line) == 1 or len(split_line) == 2:
                word_list.append(split_line[0])
            else:
                print("Wrong format of the line in the file", line)
    return word_list

if __name__ == '__main__':
    unittest.main(verbosity=3)
