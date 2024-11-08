import pytest
from bank import Account

def test_initial_balance():
    """
    Test that the initial balance of the account is 0.

    account: declaring the account to be tested

    Then assert that the balance of the account is 0.
    """
    account = Account("Kaladin")
    assert account.get_balance() == 0

def test_deposit():
       """
         Test that the deposit method adds the correct amount to the balance.

        account: declaring the account to be tested
                
        Then deposit 100 into the account and assert that the balance is 100.
       """
       account = Account("Kaladin")
       account.deposit(100)
       assert account.get_balance() == 100

def test_withdraw():
       """
       Test that the withdraw method subtracts the correct amount from the balance.
       
       account: declaring the account to be tested
       
       Then deposit 50 into the account, withdraw 45, and assert that the balance is 5.
       """
       account = Account("Kaladin")
       account.deposit(50)
       account.withdraw(45)
       assert account.get_balance() == 5

def test_deposit_negative_amount():
    """
    Test that the deposit method raises a ValueError when the amount is negative.
    
    account: declaring the account to be tested

    Then deposit -25 into the account and assert that a ValueError is raised saying 
    the deposit amount must be positive.
    """
    account = Account("Kaladin")
    assert account.deposit(-25) == ValueError("Deposit amount must be positive")
    
def test_withdraw_more_than_balance():
    """
    Test that the withdraw method raises a ValueError when the amount is greater than the balance.

    account: declaring the account to be tested
    x: contains the value of the current account balance
    Then withdraw the current balance plus 1 from the account 
    and assert that a ValueError is raised saying insufficient funds.
    """
    account = Account("Kaladin")
    x = account.get_balance()
    assert account.withdraw(x+1) == ValueError("Insufficient funds")

def test_withdraw_negative_amount():
    """
    Test that the withdraw method raises a ValueError when the amount is negative.
    account: declaring the account to be tested
    Then withdraw -25 from the account and assert that a ValueError is raised saying
    the withdrawal amount must be positive.
    """
    account = Account("Kaladin")
    assert account.withdraw(-25) == ValueError("Withdrawal amount must be positive")