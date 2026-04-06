"""hm13_job2"""


class Person:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount


class CurrencyConverter:
    # the rates are taken from NBRB on 06.04.26
    rates = {
        'BYN': 1.0,
        'EUR': 0.295,
        'USD': 0.3406
    }

    def exchange_currency(self, from_currency, from_amount, to_currency='BYN'):
        if from_currency not in self.rates:
            return f'Error: The {from_currency} currency is not supported'

        if to_currency not in self.rates:
            return f'Error: The {to_currency} currency is not supported'

        to_amount = self.rates[to_currency] / self.rates[from_currency] * from_amount
        return round(to_amount, 2), to_currency


converter = CurrencyConverter()

vasya = Person('USD', 10)
petya = Person('EUR', 5)

assert converter.exchange_currency(vasya.currency, vasya.amount) == (29.36, "BYN"), \
    "Error converting USD to BYN"
assert converter.exchange_currency(petya.currency, petya.amount) == (16.95, "BYN"), \
    "Error converting EUR to BYN"

assert converter.exchange_currency(vasya.currency, vasya.amount, 'EUR') == (8.66, "EUR"), \
    "Error converting USD to EUR"
assert converter.exchange_currency(petya.currency, petya.amount, 'USD') == (5.77, "USD"), \
    "Error converting EUR to USD"
