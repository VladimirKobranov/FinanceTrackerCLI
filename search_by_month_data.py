from datetime import datetime


def search_by_month(financesList):
    keyword = input("Enter month (leave empty for current month): \n")
    if not keyword:
        keyword = datetime.now().strftime("%B")

    matched_strings = []
    for string in financesList:
        date_str = string.split('---')[0]
        date = datetime.strptime(date_str, "%Y-%m-%d")
        month = date.strftime("%B")
        month_number = date.strftime("%m")
        if month.lower() == keyword.lower() or month.startswith(
                keyword.capitalize()) or month_number == keyword:
            matched_strings.append(string)

    if len(matched_strings) == 0:
        print('No matching strings found.')
    else:
        print(f"Matched strings for month '{keyword}':")
        for string in matched_strings:
            print(string)