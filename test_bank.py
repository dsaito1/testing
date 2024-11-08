import pytest
from bank import Account

def test_initial_balance():
    account = Account("Kaladin")
    assert account.get_balance() == 0

def test_deposit():
       account = Account("Kaladin")
       account.deposit(100)
       assert account.get_balance() == 100

def test_withdraw():
       account = Account("Kaladin")
       account.deposit(50)
       account.withdraw(45)
       assert account.get_balance() == 5

def test_deposit_negative_amount():
    account = Account("Kaladin")
    assert account.deposit(-25) == ValueError("Deposit amount must be positive")
    
def test_withdraw_more_than_balance():
    account = Account("Kaladin")
    x = account.get_balance()
    assert account.withdraw(x+1) == ValueError("Insufficient funds")
def test_withdraw_negative_amount():
    account = Account("Kaladin")
    assert account.withdraw(-25) == ValueError("Withdrawal amount must be positive")