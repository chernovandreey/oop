class People:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Student(People):
    def __init__(self, first_name, last_name, group, mark):
        super().__init__(first_name, last_name)
        self.group = group
        self.mark = mark

    def getScholarship(self):
        if self.mark == 5:
            return 2000
        else:
            return 1900

    def __str__(self):
        return f"{super().__str__()}, Группа: {self.group}, средний балл: {self.mark}"


class Aspirant(Student):
    def __init__(self, first_name, last_name, group, mark, science_work):
        super().__init__(first_name, last_name, group, mark)
        self.science_work = science_work

    def getScholarship(self):
        if self.mark == 5:
            return 2500
        else:
            return 2200

    def __str__(self):
        return f"{super().__str__()}, научная работа{self.science_work}"

students = [
    Student("Ivan", "Ivanov", "A", 4.5),
    Student("Petr", "Petrov", "B", 5),
    Aspirant("Oleg", "Olegov", "V", 4, "по космосу"),
    Aspirant("Vlad", "Vladov", "A", 5, "по земле")
]


for s in students:
    print(s)
    print(f"Стипендия составляет {s.getScholarship()}")
