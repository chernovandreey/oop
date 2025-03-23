from datetime import date

class Person:
    def __init__(self, name, country, hb):
        self.name = name
        self.country = country
        self.hb = hb

    def age_calc(self):
        now = date.today()
        age = now.year - self.hb.year
        if (now.month, now.day) < (self.hb.month, self.hb.day):
            age -= 1
        return age


age_s = input("Введите дату рождения через дифис: ")
age = date.fromisoformat(age_s)
people = Person("Axe", "UAE", age)
print(people.age_calc())
