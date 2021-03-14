#!/usr/bin/env python3

"""
011917124aee88995f7b707a31b24452
oopython
lab2
v2
necu20
2021-01-26 04:17:49
v4.0.0 (2019-03-05)

Generated 2021-01-26 05:17:50 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from json import dumps
from dbwebb import Dbwebb
from classes import Person, Address, Teacher, Student

# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - oopython
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python documentation](https://docs.python.org/3/library/index.html).
# Here you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Class relationships
#
# Practice on creating classes and relationships between them in python.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (2 points)
#
# Create a new file, put your code for the classes in it, call it
# **classes.py**.
#
# Create a new class named **Person**.  Give the class the instance
# attributes "name" and "ssn". Make "ssn" a private attribute. The values for
# the attributes should be sent to the constructor as arguments.
# Create a *get* property for "ssn".
#
# In the code below create a new variable called **per** and set it to a new
# instance of Person. Give it the name `Farseer` and ssn `578118-6946`.
#
#
# Answer with per\'s getter for ssn.
#
# Write your code below and put the answer into the variable ANSWER.
#

per = Person("Farseer", "578118-6946")


ANSWER = per.get_ssn()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (2 points)
#
# Create a new class named **Address**.  Give the class the instance
# attributes "city", "state" and "country". The values for the attributes
# should be sent to the constructor as arguments.
# Create the magic method **_\_str_\_**, in Address, it should return
# `"Address: <city> <state> <country>"` (replace the \<city\> with the value
# of the attribute city...).
#
# Create a new instance of the class Address. Initiate it with the city
# `Katar`, the state `Blekinge` and the country `Shienar` and store it in a
# variable called **per_address**.
#
# Now, go back and add the instance attribute **address** to your Person
# class. It's value should be sent as argument to constructor, give it a
# default value of and empty string, `""`.
# Create a set method for the attribute "address".
#
# Create the magic method **_\_str_\_** for Person, it should return `"Name:
# <name> SSN: <ssn> Address: <city> <state> <country>"` if the person has an
# address or, `"Name: <name> SSN: <ssn>"` if its an empty string.
#
# Use Address' string representation to get address the data.
#
# Use the set method in Person to add the newly create Address object to your
# **per** object.
#
# Answer with per's string representation.
#
# Write your code below and put the answer into the variable ANSWER.
#

per_address = Address("Katar", "Blekinge", "Shienar")
per.set_address(per_address)


ANSWER = str(per)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (2 points)
#
# Create a new class name **Teacher** make it inherit from class "Person".
# Add the instance attribute "courses" and initiate it to and empty list.
# Create the method **add_course**, it should take one argument and add it to
# the course list attribute.
# Overload the `__str__` method from the base class. It should return the
# same as the original method and add the courses to the end of the string,
# `"Name: <name> SSN: <ssn> Address: <city> <state> <country> Courses:
# <course>, <course>, ..."`. The list of courses should be comma seperated
# without one at the end. Use `super()` to access base method.
#
#
# Create a new instance of the class Teacher. Initiate it with the name
# `Skorstten` and ssn `578118-6946`.
# Use the add_course method to add the following courses, `htmlphp`, `webgl`
# and `ramverk2`.
#
#
# Answer with the Teacher object's string representation.
#
# Write your code below and put the answer into the variable ANSWER.
#


teacher = Teacher("Skorstten", "578118-6946")
teacher.add_course("htmlphp")
teacher.add_course("webgl")
teacher.add_course("ramverk2")

ANSWER = str(teacher)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (2 points)
#
# Create a new class name **Student** make it inherit from class "Person".
# Add the instance attribute "courses_grades" and initiate it to and empty
# list.
# Create the method **add_course_grade**, it should take two arguments, one
# course and a grade. Create a tuple with the two arguments and add to the
# attribute "courses_grades".
# Create the method **average_grade**. Calculate and return the students
# average grade. Ignore grades with "-" in the calculation.
#
# Create a new instance of the class Student. Initiate it with the name
# `Zimba` and ssn `516518-3442`.
# Use the add_course_grade method to add the following courses, `htmlphp`
# with grade `2`, `design` with grade `-` and `linux` with grade `5`.
#
#
# Answer with the Student object's "average_grade" method.
#
# Write your code below and put the answer into the variable ANSWER.
#

student = Student("Zimba", "516518-3442")
student.add_course_grade("html", 2)
student.add_course_grade("design", "-")
student.add_course_grade("linux", 5)


ANSWER = student.average_grade()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# In Teacher, create the *classmethod* **from_json**. This shall take one
# argument, `filename`.
# The *filename* is a json -file that contains data to create and return a
# new instance of the class Teacher.
# Use "teacher.json" to create a new instance of Teacher.
#
# Tip, import json and use `load` method.
#
# Answer with the new instance's string representation.
#
# Write your code below and put the answer into the variable ANSWER.
#

filename = "teacher.json"
teacher_fr_json = Teacher.from_json(filename)

ANSWER = str(teacher_fr_json)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# In Teacher, create the method `to_json` that returns a JSON formatted
# dictionary.
# The dictionary should have the same structure as the file used above.
#
# Answer with a json string that has an indention of 4 spaces.
#
# Write your code below and put the answer into the variable ANSWER.
#


# print(dumps(teacher_fr_json.to_json(), indent=4))

ANSWER = dumps(teacher_fr_json.to_json(), indent=4)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, True)


dbwebb.exit_with_summary()
