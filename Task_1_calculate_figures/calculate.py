import math


class Figure:
    """ Класс фигур."""
    def calculate_area(self):
        raise NotImplementedError("Переопределение метода calculate_area()")


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        """Вычисляет площадь круга по его радиусу."""
        if self.radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        return math.pi * self.radius ** 2


class Triangle(Figure):

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        if not (self.side1 + self.side2 > self.side3 and
                self.side1 + self.side3 > self.side2 and
                self.side2 + self.side3 > self.side1):
            raise ValueError('Это не треугольник!')

        if any(side <= 0 for side in (self.side1, self.side2, self.side3)):
            raise ValueError("Длины сторон должны быть положительными числами")

    def is_right_triangle(self):
        """ Является ли треугольник прямоугольным."""
        sides = sorted([self.side1, self.side2, self.side3])
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

    def calculate_area(self):
        """ Расчет площади по формуле Герона."""
        # Полупериметр треугольника
        s = (self.side1 + self.side2 + self.side3) / 2
        # Формула Герона для вычисления площади треугольника
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))


class Rectangle(Figure):
    """ Вычисляет площадь прямоугольника."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

        if any(side <= 0 for side in (self.length, self.width)):
            raise ValueError("Длины сторон должны быть положительными числами")

    def calculate_area(self):
        return self.length * self.width


def calculate_area(*args, **kwargs):
    if len(args) == 1:
        return Circle(*args).calculate_area()
    if len(args) == 2:
        return Rectangle(*args).calculate_area()
    if len(args) == 3:
        return Triangle(*args).calculate_area()
    if len(args) > 3:
        raise NotImplementedError(
            "Метод расчета площади этой фигуры не реализован!"
        )


if __name__ == "__main__":
    pass
