import unittest
from account import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        """Set up test data for each test."""
        self.account = Account("Alice", 12345, "password123")
        self.account.deposite(12345, 1000)  # Initial deposit of 1000

    def test_deposit(self):
        """Test the deposit method."""
        # Deposit 500 into the account
        self.account.deposite(12345, 500)
        self.assertEqual(self.account.balance, 1500)  # Expected balance is 1000 + 500 = 1500

        # Try depositing a negative amount
        self.account.deposite(12345, -100)
        self.assertEqual(self.account.balance, 1500)  # Balance should remain the same

    def test_withdraw(self):
        """Test the withdraw method."""
        # Withdraw 500 from the account
        self.account.withdraw(12345, 500, "password123")
        self.assertEqual(self.account.balance, 500)  # Expected balance after withdrawal

        # Try withdrawing more than the balance
        self.account.withdraw(12345, 1000, "password123")
        self.assertEqual(self.account.balance, 500)  # Balance should not change

        # Try withdrawing with wrong credentials
        self.account.withdraw(12345, 100, "wrongpassword")
        self.assertEqual(self.account.balance, 500)  # Balance should remain unchanged

    def test_check_balance(self):
        """Test the check_balance method."""
        self.account.checkbalance(12345, "password123")
        # Here, the output will be printed, but we don't assert printed output.
        # We could refactor checkbalance to return a value instead of printing.

    def test_close_account(self):
        """Test the close_account method."""
        # Close the account
        self.account.closeaccount("Alice", 12345, "password123")
        self.assertFalse(self.account.hasaccount)  # Account should be closed


    def test_display_info(self):
        """Test the display_info method."""
        self.account.display_info(12345, "password123")
        # This method prints information, but in a unit test, it's better to check for return values or side effects.
        # We would ideally want to refactor display_info to return values that can be asserted.

    def tearDown(self):
        """Clean up after each test if needed."""
        pass

if __name__ == "__main__":
    unittest.main()
