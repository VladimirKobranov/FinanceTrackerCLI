from datetime import datetime


def input_string(finances_list, currency):
    while True:
        n_value = input('Enter a value: ')
        try:
            float(n_value)
            break
        except ValueError:
            print('Enter only numbers\n')
    new_expense = input('Expense or income: ')
    if new_expense in ['expense', 'e', 't', 'true', 'exp']:
        expense_income = 'Expense'
    else:
        expense_income = 'Income'
    input_date = input("Enter a date (YY MM DD or empty-now): ")
    input_date = input_date.replace(" ", "")
    if not input_date or input_date.lower() in ["now", "today"]:
        n_date = datetime.now()
    else:
        n_date = datetime.strptime(input_date, "%y%m%d")
    formatted_date = n_date.strftime("%Y-%m-%d")
    n_description = input('Write a description: ')
    finances_list.append(f'{formatted_date}---{expense_income}---{n_value}---{currency}---{n_description}')
    print()
    print(f'Added: {formatted_date}---{expense_income}---{n_value}---{currency}---{n_description}')
