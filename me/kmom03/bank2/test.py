#!/usr/bin/env python3
""" Module for unittests """

import unittest
from shutil import copyfile
from datetime import date
from werkzeug.datastructures import ImmutableMultiDict
from account_manager import AccountManager
from person import Person
from accounts import Account, SavingsAccount

class TestBank(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase. """
    src = "static/data/test_data_orig.json"
    dst = "static/data/test_data.json"

    def setUp(self):
        """ Create object for all tests """
        # Arrange
        copyfile(TestBank.src, TestBank.dst)
        self.bank = AccountManager(TestBank.dst)

    def tearDown(self):
        """ Remove dependencies after test """
        copyfile(TestBank.src, TestBank.dst)
        self.bank = None

    def test_bank_transfer_to_account(self):
        """ Test transactions (Account). """
        imd = ImmutableMultiDict([('from_account', '1'), ('to_account', '2'), ('amount', '100')])
        self.bank.transfer(imd)
        src_account = self.bank.accounts[0]
        dst_account = self.bank.accounts[1]
        self.assertEqual(src_account.balance, 900.0)
        self.assertEqual(dst_account.balance, 1100 - 1)

    def test_bank_transfer_to_savingsaccount(self):
        """ Test transactions (SavingsAccount). """
        imd = ImmutableMultiDict([('from_account', '2'), ('to_account', '1'), ('amount', '100')])
        self.bank.transfer(imd)
        dst_account = self.bank.accounts[0]
        self.assertEqual(dst_account.balance, 1100 - 1.3)

    def test_calculate_interest_rate_account(self):
        """ Test calculation of interest rate. """
        test_account = SavingsAccount(1000, [])

        today = date.today()
        test_date = "22-09-23"
        diff = (date(22, 9, 23) - today).days
        interest_rate1 = diff * test_account.calculate_daily_interest_rate()
        interset_rate2 = AccountManager.calculate_interest_rate(test_account, test_date)
        self.assertEqual(interest_rate1, interset_rate2)

    def test_add_customer_true_and_attributes(self):
        """ Test add customer (true) and whether added attributes are correct """
        new_person = Person("Nenad", "nen")
        res = self.bank.add_customer(new_person)
        self.assertTrue(res)
        self.assertEqual(self.bank.customers[-1].name, "Nenad")
        self.assertEqual(self.bank.customers[-1].id_, "nen")

    def test_add_customer_false(self):
        """ Test add customer with existing id (false). """
        new_person = Person("Martin", "and")
        res = self.bank.add_customer(new_person)
        self.assertFalse(res)

    def test_add_account(self):
        """ Test add account. """
        new_account = Account(5000, [])
        self.bank.add_account(new_account)
        self.assertEqual(new_account, self.bank.accounts[-1])

    def test_connect_true_and_customer_id(self):
        """ Test connect customer to account (true) and if correct customer id. """
        imd = ImmutableMultiDict([('account', '2'), ('person', 'and')])
        self.assertTrue(self.bank.connect(imd))
        self.assertTrue("and" in self.bank.accounts[1].holders)
        self.assertIn("and", self.bank.accounts[1].holders)

    def test_connect_false(self):
        """ Test connect existing customer to account as holder (false). """
        imd = ImmutableMultiDict([('account', '2'), ('person', 'mar')])
        self.assertFalse(self.bank.connect(imd))
        self.assertTrue("mar" in self.bank.accounts[1].holders)
        self.assertIn("mar", self.bank.accounts[1].holders)

if __name__ == '__main__':
    unittest.main(verbosity=3)
