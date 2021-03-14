#!/usr/bin/python3
"""Main file with Handler class."""

import sys
import inspect
from unorderedlist import UnorderedList
from errors import ListIndexError, ListValueError


class Handler:
    """ Handler class """

    _OPTIONS = {
        "1": "append",
        "2": "set",
        "3": "size",
        "4": "get",
        "5": "index_of",
        "6": "print_list",
        "7": "remove",
        "q": "quit"
    }

    def __init__(self):
        """ Initialize class """
        self.list = UnorderedList()
        self.start()


    def _get_method(self, method_name):
        """
        Uses function getattr() to dynamically get value of an attribute.
        """
        return getattr(self, self._OPTIONS[method_name])


    def _print_menu(self):
        """
        Use docstring from methods to print options for the program.
        """
        menu = ""

        for key in sorted(self._OPTIONS):
            method = self._get_method(key)
            docstring = inspect.getdoc(method)

            menu += "{choice}: {explanation}\n".format(
                choice=key,
                explanation=docstring
            )

        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(menu)

    def append(self):
        """ Adds a node to the list. """
        value = input("\nAdd a value: \n>>> ")
        self.list.append(value)
        print(f"{value} has been added.")
        # print("Head.data: '" + self.list.head.data + "'")

    def set(self):
        """Replace value (data) for the node on the index place."""
        index = input("\nIndex: ")
        value = input("Value: ")
        try:
            self.list.set(index, value)
            print(f"{value} has been changed.")
        except ListIndexError as e:
            print(f"Error: {e}")

    def size(self):
        """ Shows the list length. """
        print(self.list.size())

    def get(self):
        """Get data on the index position."""
        index = input("\nEnter index value: ")
        try:
            print(self.list.get(index))
        except ListIndexError as e:
            print(f"Error: {e}")

    def index_of(self):
        """Get the first index of the data."""
        value = input("\nEnter data value: ")
        try:
            print(self.list.index_of(value))
        except ListValueError as e:
            print(f"Error: {e}")

    def print_list(self):
        """Print all nodes in the list."""
        print(self.list.print_list())

    def remove(self):
        """ Removes the first node from the list. """
        value = input("\nEnter data value: ")
        try:
            self.list.remove(value)
            print(f"{value} has been removed.")
        except (ListIndexError, ListValueError) as e:
            print(f"Error: {e}")


    @staticmethod
    def quit():
        """ Quit the program """
        sys.exit()

    def start(self):
        """ Start method """
        while True:
            self._print_menu()
            choice = input("Enter menu selection:\n-> ")

            try:
                self._get_method(choice.lower())()
            except KeyError:
                print("Invalid choice!")

            input("\nPress any key to continue ...")

if __name__ == "__main__":
    Handler()
