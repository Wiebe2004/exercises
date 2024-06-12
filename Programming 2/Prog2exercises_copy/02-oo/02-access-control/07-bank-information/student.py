class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        if amount < 1:
            raise ValueError("Cannot deposit zero or negative funds")

    def withdraw(self, amount):
        self.__balance -= amount
        if amount < 1:
            raise ValueError("Cannot withdraw zero or negative funds")
        if self.__balance < 1:
            raise ValueError("Insufficient funds")