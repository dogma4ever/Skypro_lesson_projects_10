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
		return  "300 рублей"
	else:
		return "Ошибка"


def divide(first, second):
	return first / second
