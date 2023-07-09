import json
import os

from grouped_data import group_by_month, display_grouped_data
from input_data import input_String
from search_by_month_data import search_by_month
from text_prompts import mainMessage, helpMessage, credits


def main():
    try:
        with open("FinanceList.json", "r") as infile:
            financesList = json.load(infile)
    except FileNotFoundError:
        print("The 'finances.json' file is not found.")
        print("Starting a new finance list!")
        financesList = []
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

    choice = ''
    currency = 'USD'
    while choice not in ['6', 'exit', 'quit']:
        print(mainMessage)
        choice = input('Enter index: ')
        # choice = int(input('Enter index: '))
        match choice:
            case '0' | 'help':
                clear()
                print(helpMessage)
            case '1' | 'add':
                clear()
                print('Adding new string\n')
                input_String(financesList, currency)
            case '2' | 'find':
                clear()
                if len(financesList) == 0:
                    print('List is empty!')
                else:
                    print('Looking for existing strings\n')
                    search_by_month(financesList)
            case '3' | 'all':
                clear()
                if len(financesList) == 0:
                    print('List is empty!')
                else:
                    print('Displaying all string\n')
                    sorted_list = sorted(financesList, key=lambda x: x.split('---')[0])
                    for item in sorted_list:
                        print(item)
            case '4' | 'grouped':
                clear()
                if len(financesList) == 0:
                    print('List is empty!')
                else:
                    print('Displaying grouped data\n')
                    grouped_data = group_by_month(financesList)
                    display_grouped_data(grouped_data)
            case '5' | 'clear':
                clear()
                clearQuestion = input('Do you want to clean all data? y/n: ')
                if clearQuestion == 'y':
                    financesList.clear()
                    print('Cleared!')
            case '6' | 'exit' | 'quit':
                clear()
                print('Quiting\n')
            case '7' | 'info' | 'credits':
                clear()
                print(credits)
            case _:
                print('Nothing here\n')

    print("Program Terminated!")

    with open("FinanceList.json", "w") as outfile:
        json.dump(financesList, outfile, indent=4)


if __name__ == "__main__":
    main()
