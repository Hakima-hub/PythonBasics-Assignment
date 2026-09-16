class BankAccount:
    def __init__(self,owner, balance):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount):
       if amount < 0:
           print("Deposit must be a positive amount.")
           return False
       self.__balance += amount
       print(f"Deposited ${amount}. New balance is ${self.balance}")
       return True
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Fund")
            return False
        elif amount > 0:
            self.balance -= amount
            print(f"withdrew ${amount}. New balance is ${self.balance}")
            return True

def get_balance(self):
    return self.__balance