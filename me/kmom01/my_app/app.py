#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:13:10 2021

@author: nesko

My first Flask app
"""

# Importera relevanta moduler
import traceback
from flask import Flask, render_template
from person import Person

app = Flask(__name__)

person_json_path = "static/me.json"

me = Person(person_json_path)

@app.route("/")
def main():
    """ Main route """
    return render_template("index.html")

@app.route("/about")
def about():
    """ About route """
    return render_template("about.html",
                           firstname=me.firstname,
                           familyname=me.familyname,
                           course=me.course)

@app.route("/redovisning")
def redovisning():
    """ kmom's reports """
    return render_template("redovisning.html")

@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
