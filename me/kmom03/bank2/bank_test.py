#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Test Bank.
"""

from account_manager import AccountManager

bank = AccountManager()

for customer in bank.customers:
    print(customer.id_, " ", customer.name)
for account in bank.accounts:
    print(account.id_, " ", account.type_, " ", account.balance)
