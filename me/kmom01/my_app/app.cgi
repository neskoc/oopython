#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:39:13 2021

@author: nesko

A CGI-script for python, including error handling.
"""

import traceback
from wsgiref.handlers import CGIHandler
from app import app

try:
    CGIHandler().run(app)

except Exception as e: #pylint: disable=broad-except
    print("Content-Type: text/plain;charset=utf-8")
    print("")
    print(traceback.format_exc())
