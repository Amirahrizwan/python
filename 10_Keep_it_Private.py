class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Owner:", self.owner)
        print("Balance:", self.__balance)


account = BankAccount("Riya", 5000)
account.deposit(1500)
account.show_balance()
