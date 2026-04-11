import unittest

# EXERCISE 1: Implement the BankAccount class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance


# EXERCISE 2: Write tests for BankAccount using unittest
class TestBankAccount(unittest.TestCase):
    
    def setUp(self):
        """Set up a fresh account before each test."""
        self.account = BankAccount(100)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_withdraw(self):
        self.account.withdraw(40)
        self.assertEqual(self.account.balance, 60)

    def test_withdraw_insufficient_funds(self):
        # Using context manager to test for exceptions
        with self.assertRaises(ValueError):
            self.account.withdraw(150)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

if __name__ == '__main__':
    unittest.main()
