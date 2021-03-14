#!/usr/bin/python3
"""Main file with Handler class."""

from bst import BinarySearchTree
import treevizer


test_values = [3, 8, 5, 6, 1, 0, 2, 4, 9, 7]
# test_values = [3, 10, 4, 14, 1, 8, 2, 9, 12, 18, 16, 7, 0, 11, 17, 5, 13, 6, 19, 15]
# test_values = [1, 5, 2, 4, 3, 0, 9, 7, 8, 6]
remove_seq = [5, 0, 2, 3, 4, 1, 6, 7, 8, 9]

def insert_into_bst(tree):
    """ Insert a node to the tree. """
    key = int(input("\nKey: "))
    value = input("Value: ")
    tree[key] = value
    print(f"Node {key}: {value} has been added.")
    treevizer.to_png(tree.root, png_path="bst_insert.png")

def remove_from_bst(tree):
    """ Remove a node from the tree. """
    key = int(input("\nGive me a key: "))
    try:
        print(f"{tree.remove(key)} has been removed.")
    except KeyError as e:
        print(f"Error: {e}")
    if tree.root is not None:
        treevizer.to_png(tree.root, png_path=f"bst_remove{key}.png")

def get_item(tree):
    """ Return node for given key. """
    key = int(input("\nKey: "))
    try:
        print(tree[key])
    except KeyError as e:
        print(f"Error: {e}")

def get_bst_size(tree):
    """ Shows bst length. """
    print(len(tree))

def print_inorder_bst(tree):
    """Print all nodes in the bst inorder."""
    tree.inorder_traversal_print()

def generate_test_bst(tree):
    """Generate test tree."""

    if len(tree) > 0:
        print("Removing old content ...")
        tree = None
        tree = BinarySearchTree()

    #breakpoint()
    for value in test_values:
        tree.insert(value, str(value))
    treevizer.to_png(tree.root, png_path="bst_gen.png")
    print("BST generated")

def clean_bst(tree):
    """Generate test tree."""

    for ix, key in enumerate(remove_seq):
        tree.remove(key)
        if tree.root is not None:
            treevizer.to_png(tree.root, png_path=f"bst_clean{ix}.png")
        print(f"Removed {key}")
    print("BST cleaned")

def test_in(tree):
    """ Test contain-metoden. """
    key = int(input("\nKey: "))
    print(key in tree)

def show_menu():
    """
    Show main menu.

    Returns
    -------
    inp : str
        Value (choice from the menu) given in input.

    """
    print(
        """
1) Insert a node to the tree.
2) Remove a node from the tree.
3) Return node for given key.
4) Shows bst length.
5) Print all nodes in the bst inorder.
6) Generate test tree.
7) Clean bst
8) Test contain-metoden
q) quit.
        """
        )
    inp = input("Choice: ")
    return inp


def process_choice(inp, tree):
    """
    Make a choice.

    Parameters
    ----------
    inp : str
        Choice value.

    Returns
    -------
    None

    """

    if inp == '1':
        insert_into_bst(tree)
    elif inp == '2':
        remove_from_bst(tree)
    elif inp == '3':
        get_item(tree)
    elif inp == '4':
        get_bst_size(tree)
    elif inp == '5':
        print_inorder_bst(tree)
    elif inp == '6':
        generate_test_bst(tree)
    elif inp == '7':
        clean_bst(tree)
    elif inp == '8':
        test_in(tree)
    elif inp in ('q', 'quit'):
        return True
    else:
        print('Nonexistent choice! Please try again.')
    return False

def main(tree):
    """
    Do main loop.

    Returns
    -------
    None.

    """
    finished = False
    while not finished:
        inp = show_menu()
        res = process_choice(inp, tree)
        if res:
            finished = True
    print('Have a nice day!')

if __name__ == "__main__":
    bst_obj = BinarySearchTree()
    main(bst_obj)
