class Shape:
    def area(self):
        pass

    def perimetr(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimetr(self):
        return 2 * 3.14 * self.radius


class Triangle(Shape):
    def __init__(self, base, height, x, y, z):
        self.base = base
        self.height = height
        self.x = x
        self.y = y
        self.z = z

    def area(self):
        return 0.5 * self.base * self.height

    def perimetr(self):
        return self.x + self.y + self.z


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimetr(self):
        return (self.a + self.b) * 2


calc_triangle = Triangle(1,2,3,4,5)
print(f"площадь треугольника: {calc_triangle.area()}")
print(f"периметр треугольника: {calc_triangle.perimetr()}")

calc_circle = Circle(int(input("Введите окружность: ")))
print(f"площадь круга: {calc_circle.area()}")
print(f"периметр круга: {calc_circle.perimetr()}")

calc_rectangle = Rectangle(5,4)
print(f"площадь квадрата: {calc_rectangle.area()}")
print(f"периметр квадрата: {calc_rectangle.area()}")

