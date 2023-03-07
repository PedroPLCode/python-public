"""Simple Calculator
Author: Pedro
Last update: 26.02.2023
Any comments welcome :)
"""

def main():
    
    print("\n--------Welcome--------\n"
          "---Simple-calculator---\n"
          "---------------pedro-v3")

    print_info()

    while count_again():

        user_string = input("Enter operation: ")
        list = user_string.split()

        number1 = convert_input_to_float(list[0])
        number2 = convert_input_to_float(list[2])
        operation = list[1]

        if check_input_type(number1) or check_input_type(number2):
            continue

        number1 = float(number1)
        number2 = float(number2)
        operation = str(operation)

        print(f"Result: {calculate(number1, operation, number2)}\n")


def count_again():
    """Checks if user wants to count or quit. Returns True or False"""
    while True:
        answer = input("Continue? Enter y to count or q to quit? ")
        answer = answer.strip().lower()
        if answer == "q" or answer == "quit":
            print("Ok. Quit")
            return False
            break
        elif answer == "y" or answer == "yes":
            print("\nOk. Lets count.\n")
            return True
            break
        else:
            print("Wrong answer.")


def calculate(number1, operation, number2):
    """Making a calculation ,depending on operation input. Returns result"""
    if operation == '/' and number2 == 0:
        result = str("Wrong. You can't divide by 0.")
        return result
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        result = number1 / number2
    elif operation == "%":
        result = number1 % number2
    else:
        result = str("Wrong. Operation not supported.")
        print_info()
    return result


def check_input_type(input):
    """Checks if input is float, int or string."""
    try:
        input = float(input)
        return False
    except ValueError:
        try:
            input = int(input)
            return False
        except ValueError:
            print(f"\nInput {input} is not a correct number. Looks like string.\n")
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


def print_info():
    """Prints simple info of supported operations."""
    print("\nEnter first number, operation and second number."
          "\ndivided by space (for example 2 + 3)"
          "\nsupperted operations: + - / * %\n")


main()