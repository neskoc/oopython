#!/usr/bin/env python3
"""
Contains the handler/manager class for the accounts.
"""

import json
from datetime import date
from accounts import Account, SavingsAccount
from person import Person

class AccountManager():
    """AccountManager."""
    filename = "static/data/data.json"

    def __init__(self, filename=None):
        """Define init."""
        if filename:
            AccountManager.filename = filename
        self._accounts = []
        self._customers = []
        self.load_data()

    def load_data(self):
        """Read data from json file."""
        data = {}
        with open(AccountManager.filename, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as err:
                print("JSONDecodeError", err)

        if data:
            for account in data["Accounts"]:
                if account["type"] == "Account":
                    account_from_json = Account(account["balance"], account["holders"])
                else:
                    account_from_json = SavingsAccount(account["balance"], account["holders"])
                self.add_account(account_from_json)
            for customer in data["Customers"]:
                customer_from_json = Person(customer["name"], customer["id"])
                self.add_customer(customer_from_json)

    def save_data(self):
        """Transform all data to json object and write to file."""
        data = {
            "Accounts": [],
            "Customers": []
            }
        for account in self.accounts:
            data["Accounts"].append(account.to_dict())
        for customer in self.customers:
            data["Customers"].append(customer.to_dict())

        with open(AccountManager.filename, "w") as f:
            json.dump(data, f)

    def add_account(self, account):
        """Define init."""
        self._accounts.append(account)

    def add_customer(self, customer) -> bool:
        """Add new custerm if it doesn't already exist."""
        for person in self.customers:
            if person.id_ == customer.id_:
                return False
        self._customers.append(customer)
        return True

    @property
    def accounts(self) -> list:
        """Define init."""
        return self._accounts

    @property
    def customers(self):
        """Define init."""
        return self._customers

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

    @staticmethod
    def make_new_account(acc_type, balance, holders):
        """
        Make new account.

        Parameters
        ----------
        acc_type : str
            DESCRIPTION.
        balance : str
            DESCRIPTION.
        holders : list<str>
            DESCRIPTION.

        Returns
        -------
        new_account : Account/SavingsAccount
            DESCRIPTION.

        """
        if acc_type == "Account":
            new_account = Account(balance, holders)
        else:
            new_account = SavingsAccount(balance, holders)
        return new_account

    def connect(self, data) -> bool:
        """
        Connect account to customer.

        data:
            ImmutableMultiDict([('account', '1'), ('person', 'mar')])
        """
        data_dict = data.to_dict()
        account_id = int(data_dict["account"])
        customer_id = data_dict["person"]
        holders = self.accounts[account_id - 1].holders
        if customer_id in holders:
            return False
        holders.append(customer_id)
        self.accounts[account_id - 1].holders = holders
        return True

    def get_holders(self, account_id):
        """Get holders for given account."""
        holders = []
        for holder in self.accounts[account_id - 1].holders:
            for customer in self.customers:
                if holder == customer.id_:
                    holders.append("{} - {}".format(customer.name, customer.id_))
        return holders
