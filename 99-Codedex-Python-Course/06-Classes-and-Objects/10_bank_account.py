"""
It's time to open up a bank account! 🏦

Create a file called bank_accounts.py.

Let's define a BankAccount class. Then, let's use the __init__() method to set the following attributes:

    first_name (string)
    last_name (string)
    account_id (integer)
    account_type (string)
    pin (integer)
    balance (float)

Next, let's create three methods:

    .deposit(): Add money into the account and return the new balance.
    .withdraw(): Take money out by subtracting from balance and returning the withdrawn amount.
    .display_balance(): Print the current value of balance.

Lastly, initialize a new object from the BankAccount class and use these methods to do the following:

    Deposit $96 into the account.
    Withdraw $25 from the account.
    Print the current account balance.
"""


class BankAccount:
    def __init__(self , first_name , last_name , account_id , account_type , pin , balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance  = balance


    def deposit(self , amount):
        self.balance += amount
        print(f"The amount has been deposited successfully , The updated balance is : {self.balance}")

    def withdraw(self , amount ):
        self.balance -= amount
        print(f"The amount has been debited successfully , The updated balance is : {self.balance}")

    def display_balance(self):
        print(f"The name : {self.first_name} {self.last_name} and the bank balance : {self.balance}")


# first_name , last_name , account_id , account_type , pin , balance
rahul_account = BankAccount("Rahul" , "Mishra" , 12345 , "Saving" , 4317 , 150000)

rahul_account.display_balance()
rahul_account.deposit(50000)
rahul_account.withdraw(40000)

rahul_account.display_balance()