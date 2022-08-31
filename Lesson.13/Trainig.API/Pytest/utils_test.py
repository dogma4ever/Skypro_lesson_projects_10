import pytest

from utils import double, ticket_price, divide


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