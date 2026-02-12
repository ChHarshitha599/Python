class BankAccount:
    minimum_balance = 1000

    def __init__(self,name,ac_no,phone,balance):
        self.name = name
        self.ac_no = ac_no
        self.phone = phone
        self.balance = balance

    def withdraw_money(self,amount):
        if amount <= 0:
            print("Withdrawal amount is Invalid")
        elif self.balance-amount < BankAccount.minimum_balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawal successful")
            print("Balance amount: ",self.balance)

    def deposit_money(self,amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully")
        else:
            print("Deposit amount is invalid")
    
    def display_details(self):
        print("Name: ", self.name)
        print("Account Number: ", self.ac_no)
        print("Phone: ", self.phone)
        print("Balance: ", self.balance)
        print("Minimum Balance: ", BankAccount.minimum_balance)

    @classmethod
    def update_minimum_balance(cls,new_min_balance):
        if new_min_balance >= 0:
            cls.minimum_balance = new_min_balance
            print("Updated minimum balance: ",cls.minimum_balance)
        else:
            print("Minimum balance is invalid")

b1 = BankAccount("Harshitha","1234567890","9876543210",5000)
b1.display_details()
b1.withdraw_money(3000)
b1.deposit_money(2000)
BankAccount.update_minimum_balance(2000)