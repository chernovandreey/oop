class Calculate:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            raise ZeroDivisionError("Делить на 0 нельзя")
        return self.num1 / self.num2


calk = Calculate(int(input("Введите 1-ое число: ")), int(input("Введите 2-ое число: ")))

print(calk.add())
print(calk.subtract())
print(calk.multiply())
print(calk.divide())
