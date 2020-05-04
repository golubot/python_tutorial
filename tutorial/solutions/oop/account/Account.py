from tutorial.solutions.oop.account.exception.NotEnoughFundsException import NotEnoughFundsException


class Account:
    """
    Class that represents person's account. It is constructed with default value 0 (empty account) and person's name
    is considered as unique identifier for the owner
    """
    def __init__(self, owner, balance=0):
        """
        Constructor of the account
        :param owner (str): Name of the owner
        :param balance (float): Current balance of the account
        """
        self.owner = owner
        self.balance = balance

    def __str__(self):
        """
        :return: string representation of the object's state in the time of the invocation
        """
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, dep_amt):
        """
        Adds funds to this account. Prints message if success.
        :param dep_amt (float): Amount to add
        """
        self.balance += dep_amt
        print('Deposit Accepted')

    def withdraw(self, wd_amt):
        """
        Draws funds out of this account. Prints success message or raises an exception if there are not enough funds.
        :param wd_amt (float): The amount for raising from this account
        """
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            raise NotEnoughFundsException(self.balance)