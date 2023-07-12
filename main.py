import json
import os

from grouped_data import group_by_month, display_grouped_data
from input_data import input_string
from local_convertor import local_convertor
from search_by_month_data import search_by_month
from text_prompts import mainMessage, helpMessage, creditsMessage, availableCurrencies, currency_list


def main():
    try:
        with open("FinanceList.json", "r") as infile:
            finances_list = json.load(infile)
    except FileNotFoundError:
        print("The 'finances.json' file is not found.")
        print("Starting a new finance list!")
        finances_list = []

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    choice = ''
    currency = 'USD'
    while choice not in ['8', 'exit', 'quit']:
        print(mainMessage)
        choice = input('Enter index: ')
        match choice:
            case '0' | 'help':
                clear()
                print(helpMessage)
            case '1' | 'add':
                clear()
                print('Adding new string\n')
                input_string(finances_list, currency)
            case '2' | 'find':
                clear()
                if len(finances_list) == 0:
                    print('List is empty!')
                else:
                    print('Looking for existing strings\n')
                    search_by_month(finances_list)
            case '3' | 'all':
                clear()
                if len(finances_list) == 0:
                    print('List is empty!')
                else:
                    print('Displaying all strings:\n')
                    print('------------------------------------------\n')
                    sorted_list = sorted(finances_list, key=lambda x: x.split('---')[0])
                    for item in sorted_list:
                        print(item)
            case '4' | 'grouped':
                clear()
                if len(finances_list) == 0:
                    print('List is empty!')
                else:
                    print('Displaying grouped data\n')
                    print('List of all available currencies can be found in main menu.')
                    currency_choice = input('Enter currency (Or leave for USD): ').upper()
                    print()
                    if currency_choice == '':
                        currency_choice = 'USD'
                    while currency_choice not in currency_list:
                        print('Entered currency is not in currency list')
                        print('You can watch all available currencies in main menu')
                        currency_choice = input('Enter currency again: ').upper()
                        print()
                    else:
                        if currency_choice == 'RUB':
                            print('You currency is not available at this moment.')
                            print('USD will be used\n')
                            currency_choice = 'USD'
                        else:
                            currency_choice = currency_choice
                    grouped_data = group_by_month(finances_list, currency_choice)
                    display_grouped_data(grouped_data)
            case '5' | 'currency' | 'cur':
                clear()
                print(availableCurrencies)
            case '6' | 'convertor' | 'conv':
                clear()
                print('---------Local currency convertor---------\n')
                first_input = input('First currency: ').upper()
                while first_input not in currency_list:
                    print()
                    print('Entered currency is not in currency list')
                    print('You can watch all available currencies in main menu')
                    first_input = input('Enter currency again: ').upper()
                    print()
                else:
                    if first_input == 'RUB':
                        print()
                        print('You currency is not available at this moment.')
                        print('USD will be used\n')
                        first_input = 'USD'
                    else:
                        first_input = first_input
                second_input = input('Second currency: ').upper()
                while second_input not in currency_list:
                    print()
                    print('Entered currency is not in currency list')
                    print('You can watch all available currencies in main menu')
                    second_input = input('Enter currency again: ').upper()
                    print()
                else:
                    if second_input == 'RUB':
                        print()
                        print('You currency is not available at this moment.')
                        print('USD will be used\n')
                        second_input = 'USD'
                    else:
                        second_input = second_input

                while True:
                    amount = input('Amount: ')
                    try:
                        float(amount)
                        break
                    except ValueError:
                        print('Enter only numbers\n')
                print()
                local_convertor(first_input, second_input, amount)
            case '7' | 'clear':
                clear()
                clear_question = input('Do you want to clean all data? y/n: ')
                if clear_question == 'y':
                    finances_list.clear()
                    print('Cleared!')
            case '8' | 'exit' | 'quit':
                clear()
                print('Quiting\n')
            case '9' | 'info' | 'credits':
                clear()
                print(creditsMessage)
            case _:
                print('Nothing here\n')

    print("Program Terminated!")

    with open("FinanceList.json", "w") as outfile:
        json.dump(finances_list, outfile, indent=4)


if __name__ == "__main__":
    main()
