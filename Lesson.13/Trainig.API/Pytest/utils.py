import math


def double(value):
    new_value = value * 2
    return new_value


def ticket_price(age):
    if 0 <= age < 7 or age >= 60:
        return "Бесплатно"
    elif 7 <= age < 18:
        return "100 рублей"
    elif 18 <= age < 25:
        return "200 рублей"
    elif 25 <= age < 60:
        return "300 рублей"
    else:
        return "Ошибка"


def divide(first, second):
    return first / second


def sum_of_two(first, second):
    return first + second


def get_circle_square(radius):
    if type(radius) not in [int, float]:
        raise TypeError("Должно быть int или float больше 0")
    if radius < 0:
        raise ValueError("Должно быть int или float больше 0")
    return radius ** 2 * math.pi


def get_grade(points):
    if type(points) != int: raise TypeError("Должно быть int")
    if points < 0 or points > 100: raise ValueError("Должно быть от 0 до 100")
    if points < 20:
        return 2
    elif points < 40:
        return 3
    elif points < 80:
        return 4
    else:
        return 5


class Circle:

    def __init__(self, radius):
        if type(radius) not in [int, float]:
            raise TypeError("Радиус должен быть числом, int или float")
        if radius < 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_diameter(self):
        return self.radius * 2

    def get_perimeter(self):
        return 2 * self.radius * math.pi
