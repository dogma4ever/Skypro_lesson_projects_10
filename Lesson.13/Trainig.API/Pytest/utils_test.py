import pytest

from utils import double, ticket_price, divide, sum_of_two, get_circle_square, get_grade, Circle

"""Блок тестирования обычными ассертами"""


def test_double():
    assert double(2) == 4


def test_ticket_price_0():
    assert ticket_price(0) == "Бесплатно", "Ошибка для 0 лет"


def test_ticket_price_1():
    assert ticket_price(1) == "Бесплатно", "Ошибка для 1 лет"


def test_ticket_price_7():
    assert ticket_price(7) == "100 рублей", "Ошибка для 7 лет"


def test_ticket_price_18():
    assert ticket_price(18) == "200 рублей", "Ошибка для 18 лет"


def test_ticket_price_25():
    assert ticket_price(25) == "300 рублей", "Ошибка для 25 лет"


def test_ticket_price_60():
    assert ticket_price(60) == "Бесплатно", "Ошибка для 60 лет"


def test_ticket_price_minus_1():
    assert ticket_price(-1) == "Ошибка", "Ошибка для -1 лет"


"""Блок с написанием тестового класса"""


class TestTicketPrice:

    def test_0(self):
        assert ticket_price(0) == "Бесплатно", "Ошибка для 0 лет"

    def test__1(self):
        assert ticket_price(1) == "Бесплатно", "Ошибка для 1 лет"

    def test_7(self):
        assert ticket_price(7) == "100 рублей", "Ошибка для 7 лет"

    def test_18(self):
        assert ticket_price(18) == "200 рублей", "Ошибка для 18 лет"

    def test_25(self):
        assert ticket_price(25) == "300 рублей", "Ошибка для 25 лет"

    def test_60(self):
        assert ticket_price(60) == "Бесплатно", "Ошибка для 60 лет"

    def test_minus_1(self):
        assert ticket_price(-1) == "Ошибка", "Ошибка для -1 лет"


"""Блок с проверкой ошибок"""


def test_positive_int():
    assert divide(100, 10) == 10.0

def test_negative_int():
    assert divide(-20, -5) == 4.0

def test_zero_to_int():
    assert divide(0, 2) == 0.0

def test_float():
    assert divide(2.2, 2) == 1.1

def test_type_mismatch():
    with pytest.raises(TypeError):
        divide(True, None)

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(100, 0)


"""Блок с параметризацией проверок и передачей их в асерт"""


@pytest.mark.parametrize(
    "test_input, expected",
    [(0, 0), (1, 2), (10.0, 20.0), (-3, -6), (123456789, 246913578)]
)
def test_double(test_input, expected):
    assert double(test_input) == expected


sum_of_two_parameters = [(0, 0, 0), (1, 1, 2), (-10, 10, 0)]


@pytest.mark.parametrize("first, second, expected", sum_of_two_parameters)
def test_sum_of_two(first, second, expected):
    assert sum_of_two(first, second) == expected


ticket_price_list = [(0, "Бесплатно"), (1, "Бесплатно"), (7, "100 рублей"), (18, "200 рублей"), (25, "300 рублей"), (60, "Бесплатно"), (-1, "Ошибка")]


@pytest.mark.parametrize("age, result", ticket_price_list)
def test_ticket_price(age, result):
    assert ticket_price(age) == result


"""проверка тестирования функций"""


def test_get_circle_square_zero():
    square = get_circle_square(0)
    assert square == 0, "Неверное значение для 0"


def test_get_circle_square_one():
    square = get_circle_square(1)
    assert round(square, 2) == 3.14, "Неверное значение для 1"


def test_get_circle_square_normal():
    square = get_circle_square(3)
    assert round(square, 2) == 28.27, "Неверное значение для 3"


def test_get_circle_square_value_error():
    with pytest.raises(ValueError):
        get_circle_square(-2)


def test_get_circle_square_type_error():
    with pytest.raises(TypeError):
        get_circle_square("2")


"""Параметризированая проверка с отработкой ошибок"""


grade_exceptions = [("string", TypeError), (2.1, TypeError), (-1, ValueError), (101, ValueError)]

test_grades = [(0, 2), (19, 2), (20, 3), (39, 3), (40, 4), (79, 4), (80, 5), (100, 5)]


@pytest.mark.parametrize("points, grade", test_grades)
def test_grade(points, grade):
    assert get_grade(points) == grade


@pytest.mark.parametrize("type, error", grade_exceptions)
def test_grade_exeptions(type, error):
    with pytest.raises(error):
        get_grade(type)


"""Тестирование класса Circle"""


class TestCircle:

    def test_get_radius(self):
        circle = Circle(1)
        assert circle.get_radius() == 1, "Ошибка в  радиусе"

    def test_get_diameter(self):
        circle = Circle(1)
        assert circle.get_diameter() == 2, "Ошибка в диаметре"

    def test_get_perimeter(self):
        circle = Circle(1)
        assert round(circle.get_perimeter(), 2) == 6.28, "Ошибка в периметре"

    def test_init_type_error(self):
        with pytest.raises(TypeError):
            circle = Circle("1")

    def test_init_value_error(self):
        with pytest.raises(ValueError):
            circle = Circle(-1)