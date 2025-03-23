class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimetr(self):
        return 2 * 3.14 * self.radius


radius = int(input("Введи радиус: "))
circle = Circle(radius)
area = circle.area()
perimetr = circle.perimetr()

print("Площадь:", round(area, 2))
print("Периметр:", round(perimetr, 2))