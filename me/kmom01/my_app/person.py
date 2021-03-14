#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 22:18:34 2021

@author: nesko
"""

import json
import datetime

class Person():
    "Class containing personal info"

    def __init__(self, json_path):
        person = self.read_json(json_path)
        self.firstname = person['firstname']
        self.familyname = person['familyname']
        self._birthdate = datetime.datetime.strptime(person['birthdate'], '%Y-%m-%d')
        self.picture = person['me-picture']
        self.course = person['course']

    @staticmethod
    def read_json(json_path):
        '''Read person data from json file
            {'firstname', 'familyname', 'birthdate', 'me-picture', 'course'}
        '''
        with open(json_path) as json_data:
            return json.load(json_data)

    def calculate_age(self):
        "Calculate age"
        today = datetime.date.today()
        # Using int(True) is 1 and int(False) is 0
        return today.year - self._birthdate.year - (
            (today.month, today.day) < (self._birthdate.month, self._birthdate.day)
            )
