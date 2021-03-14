#!/usr/bin/env python3

"""
1fd1eeb2f63a8550c663e9263dacc2e7
oopython
lab4
v2
necu20
2021-02-27 11:30:02
v4.0.0 (2019-03-05)

Generated 2021-02-27 12:30:02 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 4 - oopython
#
# A look into dictionaries.
#



# --------------------------------------------------------------------------
# Section 1. Dictionaries
#
# Some basics with dictionaries.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a small phonebook using a dictionary. Use the names as keys and
# numbers as values.
#
# Use
#
# > Chandler, Monica, Ross
#
# and corresponding numbers
#
# > 55523645, 55564452, 55545872
#
# Add the phonenumbers as integers. Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#

phonebook = {}
names = ['Chandler', 'Monica', 'Ross']
phonenumbers = [55523645, 55564452, 55545872]
for i, value in enumerate(names):
    phonebook[value] = phonenumbers[i]

ANSWER = phonebook

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# How many items are there in the phonebook dictionary?
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = len(phonebook)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the `get()` method on your phonebook and answer with the phonenumber of
# 'Ross'.
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER = phonebook.get('Ross')

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Get all keys from the phonebook dictionary and return them in a sorted
# list.
#
# Write your code below and put the answer into the variable ANSWER.
#

sorted_keys = sorted(phonebook.keys())

ANSWER = sorted_keys

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Get all values from the phonebook dictionary and return them in a sorted
# list.
#
# Write your code below and put the answer into the variable ANSWER.
#

sorted_values = sorted(phonebook.values())


ANSWER = sorted_values

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Use the in-operator to test if the name 'Ross' exists in the phonebook
# dictionary. Answer with the return boolean value.
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER = 'Ross' in phonebook

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a copy of the phonebook dictionary.
# Get and remove the item 'Ross' from the copied phonebook (use pop()).
# Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#

phonebook_copy = phonebook.copy()
ross = phonebook_copy.pop('Ross')

ANSWER = phonebook_copy

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (3 points)
#
# Use a for-loop to walk through the original phonebook dictionary and create
# a string representing it. Each name and number should be on its own row,
# separated by a space. The names must come in alphabetical order. Note that
# every row should end with a newline character, `\n`.
#
# Answer with the resulting string.
#
# Write your code below and put the answer into the variable ANSWER.
#

ordered_names = sorted(names)
res = ""
for i in range(len(ordered_names)):
    res += f"{names[i]} {phonebook[names[i]]}\n"

ANSWER = res

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (3 points)
#
# Convert the phonenumber to a string and add the prefix '+1-', representing
# the language code, to each phone-number.
#
# Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#

for key, value in phonebook.items():
    phonebook[key] = '+1-' + str(value)

ANSWER = phonebook

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)


dbwebb.exit_with_summary()
