class BankAccount:
    def __init__(self, owner, account_balance=0):
        self.owner = owner
        self._account_balance = account_balance
        self._transaction = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive")
        else:
            self._account_balance += amount
            self._transaction.append(f"Deposited ${amount:.2f}")
            print(f"Deposit Successful ${amount:.2f}")

    def withdrawal(self, amount):
        if amount > self._account_balance:
            print("Insufficient Balance")
        elif amount <= 0:
            print("Enter a positive number")
        else:
            self._account_balance -= amount
            self._transaction.append(f"Withdrew ${amount:.2f}")
            print(f"Withdrawal succesful ${amount:.2f}")
        
    def get_balance(self):
        return (f"Account Balance {self._account_balance}")
    
    def transaction_history(self):
        return self._transaction


owner = BankAccount("Rafsan Rubaet Hossain", 50000)
owner.deposit(500)
owner.withdrawal(500)
print(owner.get_balance())
print(owner.transaction_history())