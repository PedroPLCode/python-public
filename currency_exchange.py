"""Currency Exchange Calculator
Author: Pedro
Last update: 26.02.2023

One of my self learning, small projects.
First version had 420 lines and was using only variables, 
current version using dictionary, still trying to improve.
Any comments welcome :)
"""

currency_dict = {
    'pln': {'eur': 4.76,
            'gbp': 5.36,
            'usd': 4.45, },
    'eur': {'pln': 0.21,
            'usd': 1.07,
            'gbp': 0.89, },
    'gbp': {'pln': 0.19,
            'eur': 1.13,
            'usd': 1.20},
    'usd': {'pln': 0.22,
            'eur': 1.07,
            'gbp': 0.83, },
}


def main():
    """Main menu to choose currency to work with."""
    print("\n-----------------------------------------\n"
          "-----------Currency Exchange-------------\n"
          "---------------Calculator----------------\n"
          "---------------------------------pedro-v4\n"
          "\nHello. What currency will we exchange?\n")
    show_options(currency_dict)
    counter = 0
    while True:
        currency = str(input("\nEnter choosen currency or Q to Quit: "))
        currency = currency.lower().strip()

        if currency in get_options(currency_dict):

            next = True

            show_currencies(currency, currency_dict)
            change_currencies(currency, currency_dict)
            show_currencies(currency, currency_dict)

            while (next):
                currnecy_exchange(currency, currency_dict)

                while True:

                    next = str(input(
                        f"\nDo you want to exchange another {currency.upper()} amount? "
                        "Answer y / n "))
                    next = next.lower().strip()

                    if next == "y" or next == "yes":
                        print("Ok. Let's count again.")
                        break

                    elif next == "n" or next == 'no':
                        print("\nOk. Do you want to count another currency?\n")
                        show_options(currency_dict)
                        next = False
                        break

                    else:
                        print("Wrong answer. Please answer y / n")

        elif currency == "q" or currency == "quit" or currency == "n" or currency == "no":
            print("Ok. Quit.")
            break

        else:
            print("Wrong answer.")
            counter = counter + 1
            if counter == 3:
                print("")
                show_options(currency_dict)
                counter = 0


def show_currencies(currency, dict):
    """"Shows actual currencies for currency, taken from currencies dictionary"""
    print("\nActual currencies:")
    for key, values in dict.items():
        for key_curr, val_curr in values.items():
            if currency == key:
                print(f"Currency {key.upper()} / {key_curr.upper()}: {round(val_curr, 2)}")


def change_currencies(currency, dict):
    """Allows to change choosen currency in dictionary"""
    for key, values in dict.items():
        for key_curr, val_curr in values.items():
            if currency == key:

                while True:
                    change = str(input(f"\nDo you want to change {key.upper()} / {key_curr.upper()} currency? "
                                       "\nAnswer y / n  "))
                    change = change.lower().strip()

                    if change == "y" or change == "yes":
                        new = input(f"Enter new {key.upper()} / {key_curr.upper()} currency: ")
                        new = convert_input_to_float(new)

                        if check_input_type(new):
                            continue
                        else:
                            new = float(new)

                        if new < 0:
                            print(f"\nWrong. New {key.upper()} / {key_curr.upper()} currency can't be lower than 0"
                                  "\nDidn't change.")
                            continue

                        values[key_curr] = round(new, 2)
                        print(
                            f"Currency {key.upper()} / {key_curr.upper()} changed to {str(round(new, 2))}")
                        break

                    elif change == "n" or change == "no":
                        print(f"Currency {key.upper()} / {key_curr.upper()} not changed.")
                        break

                    else:
                        print(
                            f"Wrong answer. Currency {key.upper()} / {key_curr.upper()} not changed.")


def currnecy_exchange(currency, dict):
    """Exchanges currencies and shows results."""
    while True:
        amount = input(f"\nEnter {(currency.upper())} amount to exchange: ")
        amount = convert_input_to_float(amount)

        if check_input_type(amount):
            continue
        else:
            amount = float(amount)
            if amount < 0.1:
                print(f"Wrong. You Can't exchange less than 0.1 {currency.upper()}.")
                continue
            break
            
    print("\nExchange results:")

    for key, values in dict.items():
        for key_curr, val_curr in values.items():
            if currency == key:
                result = float(amount) / float(val_curr)
                if result < 0.01:
                    result = str("less than 0.01")
                else:
                    result = round(result, 2)

                print(
                    f"{str(round(amount, 2))} {(currency.upper())} "
                    f"equals: {str(result)} {key_curr.upper()}")


def get_options(dict):
    """Gets possible currency options from currencies dictionary and returns as list"""
    options = []
    for key in dict.keys():
        options.append(key)
    return options


def show_options(dict):
    """Shows possible currency options from currencies dictionary"""
    print("Options:")
    for key in dict.keys():
        print(key.upper())


def check_input_type(input):
    try:
        input = float(input)
        return False
    except ValueError:
        try:
            input = int(input)
            return False
        except ValueError:
            print(f"\nInput {input} is not a correct number. Looks like string."
                   "\nPlease try again.")
            return True


def convert_input_to_float(input):
    """Converts entered decimals with ',' to floats with '.' if possible."""
    if ',' in input:
        splitted = input.split(',')

        if len(splitted) == 2:
            converted = (splitted[0]+'.'+splitted[1])
            converted = float(converted)
            return converted

    else:
        return input


main()
