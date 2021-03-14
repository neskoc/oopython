#!/usr/bin/env python3
""" Module for unittests """

import unittest
from unorderedlist import UnorderedList
from node import Node
from errors import ListIndexError, ListValueError

class TestList(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase. """
    first_node_value = "one"
    second_node_value = "two"
    third_node_value = "three"
    fourth_node_value = "four"
    test_list1 = [5, 3, 4, 1, 2]
    test_list2 = ["a", "d", "b", "e", "c"]
    test_list3 = ["a", 5, 3, "e", 1, "abc", 10, 6]
    test_list1_sorted = [1, 2, 3, 4, 5]
    test_list2_sorted = ["a", "b", "c", "d", "e"]
    test_list3_sorted = [1, 3, 5, 6, 10, 'a', 'abc', 'e']

    def setUp(self):
        """ Create object for all tests """
        # Arrange
        self.list = UnorderedList()

    def tearDown(self):
        """ Remove dependencies after test """
        self.list = None

    def test_list_append(self):
        """Test append node."""
        self.list.append(TestList.first_node_value)
        self.assertIsInstance(self.list.head, Node)
        self.list.append(TestList.second_node_value)
        self.assertIsInstance(self.list.tail, Node)
        self.assertEqual(
            self.list.head.data,
            TestList.first_node_value,
            msg='Head.data: {0}'.format(self.list.head.data)
        )
        self.assertEqual(self.list.tail.data, TestList.second_node_value)
        self.assertIs(self.list.head.next, self.list.tail)

    def test_list_set_valid(self):
        """Test set node with valid index."""
        self.list.append(TestList.first_node_value)
        self.list.append(TestList.second_node_value)
        self.list.append(TestList.third_node_value)
        self.list[0] = TestList.fourth_node_value
        self.assertEqual(
            self.list.head.data,
            TestList.fourth_node_value,
            msg='Head.data: {0}'.format(self.list.head.data)
        )
        # self.assertEqual(self.list.tail.data, TestList.second_node_value)

    def test_list_set_invalid(self):
        """Test set node with invalid index."""
        with self.assertRaises(ListIndexError) as _:
            self.list[0] = TestList.first_node_value
        self.list.append(TestList.first_node_value)
        with self.assertRaises(ListIndexError) as _:
            self.list[1] = ""

    def test_list_get(self):
        """Test get node."""
        with self.assertRaises(ListIndexError) as _:
            print(self.list[0])
        self.list.append(TestList.first_node_value)
        self.list.append(TestList.second_node_value)
        self.list.append(TestList.third_node_value)
        with self.assertRaises(ListIndexError) as _:
            print(self.list[3])
        self.assertEqual(self.list[2], TestList.third_node_value)

    def test_list_index_of(self):
        """Test index_of."""
        with self.assertRaises(ListValueError) as _:
            self.list.index_of("a")
        self.list.append(TestList.first_node_value)
        self.list.append(TestList.second_node_value)
        self.list.append(TestList.third_node_value)
        self.assertEqual(self.list.index_of(TestList.third_node_value), 2)
        with self.assertRaises(ListValueError) as _:
            self.list.index_of("a")

    def test_list_remove(self):
        """Test remove element."""
        with self.assertRaises(ListIndexError) as _:
            self.list.remove("a")
        self.list.append(TestList.first_node_value)
        self.list.append(TestList.second_node_value)
        self.list.append(TestList.third_node_value)
        # remove middle value and test if shifted to the left
        self.list.remove(TestList.second_node_value)
        self.assertEqual(self.list.index_of(TestList.third_node_value), 1)
        with self.assertRaises(ListValueError) as _:
            self.list.remove(TestList.second_node_value)
        # test adding again (had problem with it before)
        self.list.append(TestList.fourth_node_value)
        self.assertEqual(self.list.index_of(TestList.fourth_node_value), 2)

    def test_list_insertionsort_all_numeric(self):
        """test_list_insertionsort_all_numeric"""
        for node in self.test_list1:
            self.list.append(node)
        self.list.insertionsort()
        res_list = []
        for i in range(len(self.list)):
            res_list.append(self.list[i])
        self.assertEqual(self.test_list1_sorted, res_list)

    def test_list_insertionsort_all_strings(self):
        """test_list_insertionsort_all_strings"""
        for node in self.test_list2:
            self.list.append(node)
        self.list.insertionsort()
        res_list = []
        for i in range(len(self.list)):
            res_list.append(self.list[i])
        self.assertEqual(self.test_list2_sorted, res_list)

    def test_list_insertionsort_mixed(self):
        """test_list_insertionsort_mixed"""
        for node in self.test_list3:
            self.list.append(node)
        self.list.insertionsort()
        res_list = []
        for i in range(len(self.list)):
            res_list.append(self.list[i])
        self.assertEqual(self.test_list3_sorted, res_list)

    def test_list_recursive_insertionsort_all_numeric(self):
        """test_list_recursive_insertionsort_all_numeric"""
        for node in self.test_list1:
            self.list.append(node)
        self.list.recursive_insertionsort()
        res_list = []
        for i in range(len(self.list)):
            res_list.append(self.list[i])
        self.assertEqual(self.test_list1_sorted, res_list)

    def test_list_recursive_insertionsort_all_strings(self):
        """test_list_recursive_insertionsort_all_strings"""
        for node in self.test_list2:
            self.list.append(node)
        self.list.recursive_insertionsort()
        res_list = []
        for i in range(len(self.list)):
            res_list.append(self.list[i])
        self.assertEqual(self.test_list2_sorted, res_list)

    def test_list_recursive_insertionsort_mixed(self):
        """test_list_recursive_insertionsort_mixed"""
        for node in self.test_list3:
            self.list.append(node)
        self.list.recursive_insertionsort()
        res_list = []
        for i in range(len(self.list)):
            res_list.append(self.list[i])
        self.assertEqual(self.test_list3_sorted, res_list)

if __name__ == '__main__':
    unittest.main(verbosity=3)
