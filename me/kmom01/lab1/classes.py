#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 17:40:24 2021

@author: nesko
"""

class Cat():
    "Cat class"
    nr_of_paws = 4

    def __init__(self, eye_color, name):
        self.eye_color = eye_color
        self.name = name
        self._lives_left = -1

    def get_lives_left(self):
        "Cat lives left"
        return self._lives_left

    @property
    def lives_left(self):
        "Cat lives left"
        return self._lives_left

    def set_lives_left(self, lives_left):
        "Set cat lives left"
        self._lives_left = lives_left

    @lives_left.setter
    def lives_left(self, lives_left):
        "Cat lives left"
        if lives_left >= -1:
            self._lives_left = lives_left
        else:
            print("Can can't have less then -1 lives left. -1 means it is dead.")

    def description(self):
        "Describe cat"
        tmp_str = f"My cats name is {self.name}, has {self.eye_color} eyes"
        return tmp_str + f" and {self._lives_left} lives left to live."

class Duration():
    "Cat class"

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
        "Display duration as string"
        return "{:0>2d}-{:0>2d}-{:0>2d}".\
            format(self.hours, self.minutes, self.seconds)

    @staticmethod
    def duration_to_sec(time_as_str):
        "Convert duration to seconds"
        time_split = time_as_str.split("-")
        nr_of_seconds = (60 * (60 * int(time_split[0]) +
                               int(time_split[1])) +
                         int(time_split[2]))
        return nr_of_seconds

    def __add__(self, other):
        return (Duration.duration_to_sec(self.display()) +
                Duration.duration_to_sec(other.display()))

    def __iadd__(self, other):
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds
        return self

    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        if self.minutes < other.minutes:
            return True
        if self.seconds < other.seconds:
            return True
        return False
