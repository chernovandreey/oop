from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_noise(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class Dog(Animal):
    def make_noise(self):
        print(f"{self.name} гавкает")

    def eat(self):
        print(f"{self.name} любит кости")

    def get_description(self):
        return f"Это собака по кличке {self.name}"


class Cat(Animal):
    def make_noise(self):
        print(f"{self.name} мяукает")

    def eat(self):
        print(f"{self.name} любит рыбу")

    def get_description(self):
        return f"Это кошка по кличке {self.name}"


class Bear(Animal):
    def make_noise(self):
        print(f"{self.name} рычит")

    def eat(self):
        print(f"{self.name} любит малину")

    def get_description(self):
        return f"Это медведь по кличке {self.name}"


class Doctor:
    def treat_animal(self, animal):
        print(f"ветеринар лечит: {animal.name}. Описание: {animal.get_description()}")


animals = [
    Dog("Tor"),
    Cat("Myrka"),
    Bear("Grizzly")
]

vet = Doctor()

for animal in animals:
    vet.treat_animal(animal)

print("--------")

for animal in animals:
    animal.make_noise()
    animal.eat()
