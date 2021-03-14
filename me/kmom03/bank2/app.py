#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Minimal Flask application, including useful error handlers.
"""

from datetime import date, timedelta
from flask import Flask, render_template, request
from account_manager import AccountManager
from person import Person

app = Flask(__name__)
app.jinja_env.line_statement_prefix = '#'
bank = AccountManager()


@app.route("/")
def main():
    """
    Home route
    Shows a table of all accounts and their information.
    """
    return render_template("index.html", accounts=bank.accounts, customers=bank.customers)


@app.route("/transfer", methods=["POST", "GET"])
def transfer():
    """
    Transaction route
    Displays a form where you can transfer balance.
    """
    message = None
    if request.method == "POST":
        bank.transfer(request.form)
        bank.save_data()
        message = "Moved ${amount} from account #{from_} to #{to}".format(
            amount=request.form["amount"],
            from_=request.form["from_account"],
            to=request.form["to_account"],
        )

    return render_template(
        "transfer.html",
        accounts=bank.accounts,
        message=message
    )


@app.route("/connect", methods=["POST", "GET"])
def connect():
    """
    Route to connect a person/customer to an account
    """
    message = None
    if request.method == "POST":
        if bank.connect(request.form):
            bank.save_data()
            message = "Connected account #{account} to customer '{customer}'".format(
                account=request.form["account"],
                customer=request.form["person"],
            )
        else:
            message = "Account #{account} is already connected to the customer '{customer}'".format(
                account=request.form["account"],
                customer=request.form["person"],
            )

    return render_template(
        "connect.html",
        accounts=bank.accounts,
        persons=bank.customers,
        message=message
    )


@app.route('/account/<int:account_id>', methods=["POST", "GET"])
def account(account_id):
    """
    Account route
    Takes an account id and displays its "own" page.
    """
    interests = None
    current_account = bank.get_account_by_id(account_id)
    holders = bank.get_holders(account_id)
    date_ = date.today() + timedelta(days=1)

    if request.method == "POST":
        date_ = request.form["calculation_date"]
        interests = bank.calculate_interest_rate(current_account, date_)

    return render_template(
        "account.html",
        account=current_account,
        holders=holders,
        time=date_,
        interests=interests
    )

@app.route("/add/<string:what>", methods=["POST", "GET"])
def add(what):
    """
    Route to add accounts or persons
    - /add/person  returns a create form for the class Person
    - /add/account returns a create form for the Account classes
    """
    message = None

    if request.method == "POST":
        if what == "person":
            name = request.form["name"]
            id_ = request.form["id"]
            if bank.add_customer(Person(name, id_)):
                message = "{} has been added".format(name)
            else:
                message = "Error: The id '{}' already exists.".format(id_)
        elif what == "account":
            acc_type = request.form["type"]
            balance = float(request.form["balance"])
            bank.add_account(AccountManager.make_new_account(acc_type, balance, []))
            message = "A new {} has been added".format(acc_type)
        else:
            raise "Unknown action"
        bank.save_data()

    account_types = [{"id_": "Account"}, {"id_": "SavingsAccount"}]
    return render_template(
        "add.html",
        what=what,
        account_types=account_types,
        message=message
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
