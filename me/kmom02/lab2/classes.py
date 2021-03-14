# -*- coding: utf-8 -*-

"""
classes.py file.

@nesko
"""

import json


class Person():
    """
    Create Person class.

    Second line
    """

    def __init__(self, name, ssn, address=""):
        """
        Init method.

        Parameters
        ----------
        name : str
            DESCRIPTION.
        ssn : str
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.name = name
        self._ssn = ssn
        self.address = address

    def get_ssn(self):
        """
        Getter ssn method.

        Returns
        -------
        str
            ssn getter.

        """
        return self._ssn

    def set_address(self, address):
        """
        Setter address method.

        Parameters
        ----------
        address : Address
            DESCRIPTION.

        Returns
        -------
        None.
        """
        self.address = address

    def __str__(self):
        """
        Just a magic method.

        Returns
        -------
        str
            DESCRIPTION.

        """
        if self.address != "":
            address_str = str(self.address)
        else:
            address_str = ""
        ssn = self.get_ssn()
        return f"Name: {self.name} SSN: {ssn} {address_str}"


class Address():
    """
    Definition of Address class.

    Second line
    """

    def __init__(self, city, state, country):
        self.city = city
        self.state = state
        self.country = country

    def __str__(self):
        """Define string method."""
        return f"Address: {self.city} {self.state} {self.country}"


class Teacher(Person):
    """Some class."""

    def __init__(self, *args, **kwargs):
        self.courses = []
        super(Teacher, self).__init__(*args, **kwargs)

    def add_course(self, course):
        """Some method."""
        self.courses.append(course)

    def __str__(self, *args, **kwargs):
        """Some method."""
        super_str = str(super().__str__(*args, **kwargs))
        self_str = "Courses:"
        first = True
        for course in self.courses:
            if first:
                comma_prefix = ""
                first = False
            else:
                comma_prefix = ","
            self_str += comma_prefix + " " + course
        return super_str + self_str

    @classmethod
    def from_json(cls, filename):
        """Some method."""
        with open(filename, 'r') as fh:
            json_data = json.load(fh)
        # print(json_data)
        teacher = Teacher(json_data["name"], json_data["ssn"])
        for course in json_data["courses"]:
            teacher.add_course(course)
        return teacher

    def to_json(self):
        """Some method."""
        teacher = {}
        teacher["name"] = self.name
        teacher["ssn"] = self.get_ssn()
        teacher["courses"] = self.courses
        return teacher

class Student(Person):
    """
    Definition of Student class.

    Second line
    """

    def __init__(self, *args, **kwargs):
        """Some method."""
        self.courses_grades = []
        super(Student, self).__init__(*args, **kwargs)

    def add_course_grade(self, course, grade):
        """Some method."""
        self.courses_grades.append({"course": course, "grade": grade})

    def average_grade(self):
        """Some method."""
        avg = 0
        count = 0
        for cour_gr in self.courses_grades:
            if cour_gr["grade"] != "-":
                avg += cour_gr["grade"]
                count += 1
        return avg / count
