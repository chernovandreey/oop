class Bank:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        if not isinstance(value, (int,float)):
            raise ValueError("баланс должен содержать числа")
        self.__balance = value

    @my_balance.deleter
    def my_balance(self):
        del self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Внесено {amount} рублей. Новый баланс: {self.__balance} рублей.")
        else:
            print("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Снято {amount} рублей. Остаток на счете: {self.__balance} рублей.")
        elif amount > self.__balance:
            print("Недостаточно средств на счете.")
        else:
            print("Сумма снятия должна быть положительной.")


acc1 = Bank("axe", 1500)
print(acc1.my_balance)
acc1.deposit(1500)
print(acc1.my_balance)
acc1.withdraw(2000)
print(acc1.my_balance)
