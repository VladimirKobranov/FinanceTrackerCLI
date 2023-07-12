from datetime import datetime
from decimal import Decimal, ROUND_DOWN

from forex_python.converter import CurrencyRates

c = CurrencyRates()


def group_by_month(finances_list, currency_choice):
    print('Loading...\n')
    grouped_data = {}
    for item in finances_list:
        parts = item.split('---')
        date_str, expense_income, value, *rest = parts
        date_parts = date_str.split('-')
        month = datetime.strptime(date_parts[1], "%m").strftime("%B")
        year = date_parts[0]
        month_year = f"{month} {year}"
        description = ''

        value = c.convert('USD', currency_choice, Decimal((float(value))))
        value = value.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
        currency = currency_choice
        if month_year not in grouped_data:
            grouped_data[month_year] = []
        if expense_income == 'Expense':
            value = float(value) * -1
        if rest:
            # currency = rest[0]
            description = '---'.join(rest[1:])
            grouped_data[month_year].append(
                f"{date_parts[2]}---{expense_income}---{value}---{currency}---{description}")
        else:
            grouped_data[month_year].append(f"{date_parts[2]}---{expense_income}---{value}---{description}")
    return grouped_data


def display_grouped_data(grouped_data):
    overall_sum = Decimal('0.0')
    overall_expense = Decimal('0.0')
    overall_income = Decimal('0.0')
    sorted_months = sorted(grouped_data.keys(), key=lambda x: datetime.strptime(x, "%B %Y"), reverse=False)
    currency = ''
    for month in sorted_months:
        values = grouped_data[month]
        print(f"{month}:")
        for value in values:
            parts = value.split('---')
            if len(parts) == 4:
                date, expense_income, amount, description = parts
            else:
                date, expense_income, amount, currency, description = parts
            print(f"{date}---{expense_income}---{amount}---{currency}---{description}")
            expense_income = expense_income
            amount = Decimal(amount)
            if expense_income == 'Expense':
                overall_expense += amount
            else:
                overall_income += amount
        sum_value = sum(Decimal(value.split('---')[2]) for value in values)
        print("Sum:", sum_value if sum_value >= Decimal('0') else f"-{abs(sum_value)}", currency)
        overall_sum += sum_value
        print()
    print('Expenses:', abs(overall_expense), currency)
    print("Income:", abs(overall_income), currency)
    print("Total:", overall_sum.quantize(Decimal('0.00'), rounding=ROUND_DOWN), currency)
