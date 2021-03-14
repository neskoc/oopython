#!/usr/bin/env python3

"""
04a7e587df48d8be84231deb8bc24108
oopython
lab3
v2
necu20
2021-02-17 02:51:30
v4.0.0 (2019-03-05)

Generated 2021-02-17 03:51:31 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - Recursion
#
# If you need to peek at examples or just want to know more, take a look at
# the page: https://docs.python.org/3/library/index.html. Here you will find
# everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Simple recursion
#
# Practice on creating recursive functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a recursive function in the code below that calculates the sum of
# the numbers `19` up to `37`.
#
# Answer with the sum.
#
# Write your code below and put the answer into the variable ANSWER.
#

def calc_recursive_sum(start=19, end=37):
    "calc_recursive_sum"
    if start < end:
        return start + end + calc_recursive_sum(start + 1, end - 1)
    if start > end:
        return 0
    return start

res = calc_recursive_sum()

ANSWER = res

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create a recursive function in the code below that searches for the maximum
# element of a list and returns that number.
# Find the maximum value in the list `[3, 4, 2, 9, 1, 8, 2, 40, 6]`.
#
# Answer with the maximumx value.
#
# Write your code below and put the answer into the variable ANSWER.
#

global_list = [3, 4, 2, 9, 1, 8, 2, 40, 6]
def recursive_max(mylist):
    "lab3"
    if len(mylist) == 1:
        return mylist[0]
    if mylist[0] > recursive_max(mylist[1:]):
        return mylist[0]
    return recursive_max(mylist[1:])

ANSWER = recursive_max(global_list)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a recursive function in the code below that searches a list for a
# number and returns the index of the number.
# Find the index of `9` in the list `[3, 4, 2, 9, 1, 8, 2, 40, 6]`.
# If the number cant be found, return -1.
#
# Answer with the index.
#
# Write your code below and put the answer into the variable ANSWER.
#

def recursive_find(mylist, number=9, index=0):
    "lab3"
    if mylist[index] == number:
        return index
    if index < len(mylist) - 1:
        return recursive_find(mylist, number, index + 1)
    return -1

ANSWER = recursive_find(global_list)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Use the function from the previous assignment to find the number `12` in
# the list `[3, 4, 2, 9, 1, 8, 2, 40, 6]`.
#
# Answer with the index.
#
# Write your code below and put the answer into the variable ANSWER.
#



ANSWER = recursive_find(global_list, 12)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a recursive function in the code below that calculates `4` to the
# power of `5`.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

def recursive_pow(value, n):
    "lab3"
    if n == 1:
        return value
    return value * recursive_pow(value, n - 1)

ANSWER = recursive_pow(4, 5)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Create a recursive function in the code below that turns a string
# backwards. Turn the string "Switchy mc switch" backwards.
#
# Answer with the backward string.
#
# Write your code below and put the answer into the variable ANSWER.
#

mystring = "Switchy mc switch"

def recursive_reverse_str(string):
    "lab3"
    if len(string) == 1:
        return string
    return string[-1] + recursive_reverse_str(string[0:-1])

res = recursive_reverse_str(mystring)
# print(res)

ANSWER = res

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a recursive function in the code below that calculates the "lowest
# common multiple" between two numbers.
# It should return the smallest positive integer that is divisible by both
# "11" and "3".
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

def recursive_lowest_common_multiple(nr=1, div1=3, div2=11):
    "lab3"
    if nr % div1 == 0 and nr % div2 == 0:
        return nr
    return recursive_lowest_common_multiple(nr + 1)

ANSWER = recursive_lowest_common_multiple(11)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)


dbwebb.exit_with_summary()
