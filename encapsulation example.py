class BankAccount:
    def __init__(self, initial_balance=0):
        
        self.__balance = initial_balance

    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    
    def get_balance(self):
        return self.__balance


account = BankAccount(100)  
account.deposit(50)         
account.withdraw(30)        
print(f"Final balance: ${account.get_balance()}")
