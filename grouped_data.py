from datetime import datetime


def group_by_month(finances_list):
    grouped_data = {}
    for item in finances_list:
        parts = item.split('---')
        date_str, expense_income, value, *rest = parts
        date_parts = date_str.split('-')
        month = datetime.strptime(date_parts[1], "%m").strftime("%B")
        year = date_parts[0]
        month_year = f"{month} {year}"

        if month_year not in grouped_data:
            grouped_data[month_year] = []
        if expense_income == 'Expense':
            value = float(value) * -1
        if rest:
            currency = rest[0]
            description = '---'.join(rest[1:])
            grouped_data[month_year].append(
                f"{date_parts[2]}---{expense_income}---{value}---{currency}---{description}")
        else:
            grouped_data[month_year].append(f"{date_parts[2]}---{expense_income}---{value}---{description}")
    return grouped_data


def display_grouped_data(grouped_data):
    overall_sum = 0.0
    overall_expense = 0.0
    overall_income = 0.0
    sorted_months = sorted(grouped_data.keys(), key=lambda x: datetime.strptime(x, "%B %Y"), reverse=False)

    for month in sorted_months:
        values = grouped_data[month]
        print(f"{month}:")
        for value in values:
            parts = value.split('---')
            if len(parts) == 4:
                date, expense_income, amount, description = parts
                currency = ''
            else:
                date, expense_income, amount, currency, description = parts
            print(f"{date}---{expense_income}---{amount}---{currency}---{description}")
            expense_income = expense_income
            amount = float(amount)
            if expense_income == 'Expense':
                overall_expense += amount
            else:
                overall_income += amount
        sum_value = sum(float(value.split('---')[2]) for value in values)
        print("Sum:", sum_value if sum_value >= 0 else f"-{abs(sum_value)}")
        overall_sum += sum_value
        print()
    print('Expenses:', abs(overall_expense), currency)
    print("Income:", abs(overall_income), currency)
    print("Total:", overall_sum if overall_sum >= 0 else f"-{abs(overall_sum)}", currency)
