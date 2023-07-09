from datetime import datetime


def input_String(financesList, currency):
    nValue = float(input('Enter a value: '))
    newExpense = input('Expense or income: ')
    if newExpense in ['expense', 'e', 't', 'true', 'exp']:
        expense_income = 'Expense'
    else:
        expense_income = 'Income'
    inputDate = input("Enter a date (YY MM DD or empty-now): ")
    inputDate = inputDate.replace(" ", "")
    if not inputDate or inputDate.lower() in ["now", "today"]:
        nDate = datetime.now()
    else:
        nDate = datetime.strptime(inputDate, "%y%m%d")
    formatted_date = nDate.strftime("%Y-%m-%d")
    nDescription = input('Write a description: ')
    financesList.append(f'{formatted_date}---{expense_income}---{nValue}---{currency}---{nDescription}')
    print()
    print(f'Added: {formatted_date}---{expense_income}---{nValue}---{currency}---{nDescription}')
