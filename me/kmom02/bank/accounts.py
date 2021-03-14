"""
Account classes.


Account:
    account_number = 1
    transaction_fee = 0.01

SavingsAccount:
    interest_rate = 0.0015
    transaction_fee = 0.013
"""

class Account():
    """Account class."""
    account_number = 1
    transaction_fee = 0.01

    def __init__(self, balance):
        """Define init."""
        self._balance = balance
        self._id = Account.account_number
        self._type = "Account"
        Account.account_number += 1

    @property
    def id_(self) -> int:
        """Get account _id."""
        return self._id

    @property
    def balance(self) -> float:
        """Get account _balance."""
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Set account _balance."""
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Balance is not allowed to be less then zero")

    @classmethod
    def calculate_transaction_fee(cls, amount) -> float:
        """Calculate transaction fee."""
        transacton_fee = cls.transaction_fee * amount
        return transacton_fee

    @property
    def type_(self) -> str:
        """Get type."""
        return self._type

    def to_dict(self):
        """Transform data to a dict for saving in json file"""
        return {"type": self.type_, "balance": self.balance}


class SavingsAccount(Account):
    """Class SavingsAccount."""
    interest_rate = 0.0015
    transaction_fee = 0.013

    def __init__(self, balance):
        """Define init."""
        super().__init__(balance)
        self._type = "SavingsAccount"

    def calculate_daily_interest_rate(self) -> float:
        """Calculate daily intrest rate."""
        daily_intrest_rate = SavingsAccount.interest_rate * self.balance / 365
        return daily_intrest_rate
