class BankAccount:

    def __init__(self, accountnumber, customername, balance):
        self.balance = 100000
        self.accountnumber = accountnumber
        self.customername = customername

    def deposit(self, amount):
        self.balance+=amount

    def withdrawal(self, amount):
        self.withdrawal+=amount

Test_Account=BankAccount(123,"Fred Jones",5684257)
        
print(Test_Account.customername) 
print(Test_Account.balance)
Test_Account.deposit(250)
print(Test_Account.balance)