class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print(f"Your account has been deposited with {money}. Your balance is {self.balance}. \n")

    def withdraw(self, withdraw_money):
        if self.balance >= withdraw_money:
            self.balance -= withdraw_money
            print(f"You have withdrawn {withdraw_money} from your account. Your balance is {self.balance}. \n")
        else:
            print(f"Insufficient funds in your account to withdraw {withdraw_money}. Your balance is {self.balance}. \n")
    

operation = Account("Ademi",10000)
operation.deposit(5000)
operation.withdraw(15000)
operation.withdraw(100)
operation.deposit(356)
operation.withdraw(355)