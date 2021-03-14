#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Minimal Flask application, including useful error handlers.
"""

from flask import Flask, render_template, request
from trie import Trie, SearchMiss

filename = 'frequency.txt'

app = Flask(__name__)
trie = Trie()
trie.generate_trie(filename)


@app.route("/")
def main():
    """
    Home route
    """
    return render_template("index.html")


@app.route("/all_words", methods=["POST", "GET"])
def all_words():
    """
    Prints all words in dictionary
    """
    message = None

    return render_template(
        "all_words.html",
        words=trie.get_sorted_words(),
        message=message
    )


@app.route('/search', methods=["POST", "GET"])
def search():
    """
    Account route
    Takes an account id and displays its "own" page.
    """
    message = None
    word = ""

    if request.method == "POST":
        word = request.form["search"]
        try:
            if word in trie:
                message = f'Word "{word}" with frequency {trie.freq} is found'
        except SearchMiss:
            message = f'Word "{word}" is not found'
    return render_template(
        "search.html",
        message=message,
        word=word
    )


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
    #pylint: disable=unused-argument,import-outside-toplevel
    import traceback
    return "<p>Flask 500<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run(debug=True)
