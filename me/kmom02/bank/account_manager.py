#!/usr/bin/env python3
"""
Contains the handler/manager class for the accounts.
"""

import json
from datetime import date
from accounts import Account, SavingsAccount

class AccountManager():
    """AccountManager."""
    filename = "static/data/data.json"

    def __init__(self):
        """Define init."""
        self._accounts = []
        self.load_data()

    def load_data(self):
        """Read data from json file."""
        data = {}
        with open(AccountManager.filename, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print("Empty file")

        if data:
            for account in data["Accounts"]:
                if account["type"] == "Account":
                    account_from_json = Account(account["balance"])
                else:
                    account_from_json = SavingsAccount(account["balance"])
                self.add_account(account_from_json)

    def save_data(self):
        """Transform all data to json object and write to file."""
        data = {"Accounts": []}
        for account in self.accounts:
            data["Accounts"].append(account.to_dict())

        with open(AccountManager.filename, "w") as f:
            json.dump(data, f)

    def add_account(self, account):
        """Define init."""
        self._accounts.append(account)

    @property
    def accounts(self):
        """Define init."""
        return self._accounts

    def get_account_by_id(self, id_) -> Account:
        """Define init."""
        accounts = self.accounts
        return accounts[int(id_) - 1]

    def transfer(self, data):
        """
        Transfer amount from account1 to account2.

        data:
            ImmutableMultiDict([('from_account', '1'), ('to_account', '2'), ('amount', '100')])
        """
        data_dict = data.to_dict()
        if data_dict["from_account"] != data_dict["to_account"]:
            accounts = self.accounts
            amount = int(data_dict["amount"])
            from_account = accounts[int(data_dict["from_account"]) - 1]
            accounts[int(data_dict["from_account"]) - 1].balance -= amount

            to_account = self.accounts[int(data_dict["to_account"]) - 1]
            to_account.balance += amount - from_account.calculate_transaction_fee(amount)
            self.accounts[int(data_dict["to_account"]) - 1].balance = to_account.balance

    @staticmethod
    def calculate_interest_rate(account, date_) -> float:
        """Define init."""
        today = date.today()
        date_split = date_.split("-")
        yy = int(date_split[0])
        mm = int(date_split[1])
        dd = int(date_split[2])

        diff = (date(yy, mm, dd) - today).days
        interest_rate = diff * account.calculate_daily_interest_rate()
        return interest_rate
