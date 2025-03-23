class Car:
    def __init__(self, brand, car_class, weight, driver, engine):
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self):
        print("Поехали")

    def stop(self):
        print("Тормози")

    def turn_right(self):
        print("Направо")

    def turn_left(self):
        print("Налево ")

    def __str__(self):
        return f"Машина: {self.brand} класса: {self.car_class}, вес: {self.weight}, Мотор: {self.engine}, Водитель: {self.driver}"

class Engine:
    def __init__(self, power, company):
        self.power = power
        self.company = company

    def __str__(self):
        return f"Мощность движка: {self.power}, производитель: {self.company}"


class Person:
    def __init__(self, full_name):
        self.full_name = full_name

    def __str__(self):
        return self.full_name


class Driver(Person):
    def __init__(self, full_name, experience):
        super().__init__(full_name)
        self.experience = experience

    def __str__(self):
        return f"Водитель: {self.full_name} со стажем {self.experience} лет"


class Lorry(Car):
    def __init__(self, brand, car_class, weight, driver, engine, max_weight):
        super().__init__(brand, car_class, weight, driver, engine)
        self.max_weight = max_weight

    def __str__(self):
        return (f"Машина: {self.brand} класса: {self.car_class}, вес: {self.weight}, Мотор: {self.engine},"
                f"Водитель: {self.driver}, максимальная грузоподъемность: {self.max_weight}")


class SportCar(Car):
    def __init__(self, brand, car_class, weight, driver, engine, max_speed):
        super().__init__(brand, car_class, weight, driver, engine)
        self.max_speed = max_speed

    def __str__(self):
        return (f"Машина: {self.brand} класса: {self.car_class}, вес: {self.weight}, Мотор: {self.engine},"
                f"Водитель: {self.driver}, максимальная скорость: {self.max_speed}")


engine1 = Engine(400, "toyota")
driver1 = Driver("Han", 20)
kamaz1 = Lorry("маз", "грузовой", 5000, driver1, engine1, 20000)
naskar1 = SportCar("supra", "спортивная", 1500, driver1, engine1, 370)

print(kamaz1)
print("----------------------")
print(naskar1)
