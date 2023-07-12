import math

from forex_python.converter import CurrencyRates

c = CurrencyRates()


def local_convertor(first_input, second_input, amount):
    print('Loading...\n')
    first_currency = str(first_input).upper()
    second_currency = str(second_input).upper()
    first_amount = amount

    second_amount = c.convert(first_currency, second_currency, float(first_amount))
    second_amount = math.floor(second_amount * 100) / 100

    conversion_rate = c.get_rate(first_currency, second_currency)
    conversion_rate = math.floor(conversion_rate * 100) / 100

    print(f'{first_currency}: {first_amount}')
    print(f'{second_currency}: {second_amount}')
    print(f'Conversion rate: {conversion_rate}')
