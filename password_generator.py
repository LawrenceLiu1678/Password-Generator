import random
import string

"""
@author: Lawrence Liu
@date  : January 8th, 2022
@version: 1.0

This program outputs a password by asking several questions to the user, such as wanting symbols, numbers, and
uppercase letters.
"""


def main():
    """
    Various inputs by the user in order to generate a password
    """

    length = generate_length()
    symbol = generate_symbol()
    number = generate_number()
    lower = generate_lower()
    upper = generate_upper()
    exclude_c = remove_similar_characters()
    exclude_a = remove_ambiguous_characters()

    password = generate_password(length, symbol, number, lower, upper, exclude_c, exclude_a)
    generate_message(password)


# Generates the length of the password
def generate_length():
    user_input_value = int(input("Input the length of the password: "))

    while True:
        if user_input_value > 0 and isinstance(user_input_value, int):
            return user_input_value
        elif user_input_value <= 0 or not isinstance(user_input_value, int):
            print("The length must be greater than 0 and a number.")
            return generate_length()
        else:
            break


# Generates all symbols (if the user desires it)
def generate_symbol():
    user_input_symbol = input("Would you like to include symbols (Y/N)? ")

    while True:
        if user_input_symbol.upper() == "Y" and len(user_input_symbol) == 1:
            return string.punctuation
        elif user_input_symbol.upper() == "Y" and len(user_input_symbol) != 1:
            print("You can only do ONE 'Y' or 'N'")
        else:
            return "N"


# Generates 0-9 (if the user wants it)
def generate_number():
    user_input_number = input("Would you like to include numbers (Y/N)? ")

    while True:
        if user_input_number.upper() == "Y" and len(user_input_number) == 1:
            return string.digits
        elif user_input_number.upper() == "Y" and len(user_input_number) != 1:
            print("You can only do ONE 'Y' or 'N'")
        else:
            return "N"


# Generates all letters in lowercase (if the user wants it)
def generate_lower():
    user_input_lower = input("Would you like to include lowercase (Y/N)? ")

    while True:
        if user_input_lower.upper() == "Y" and len(user_input_lower) == 1:
            return string.ascii_lowercase
        elif user_input_lower.upper() == "Y" and len(user_input_lower) != 1:
            print("You can only do ONE 'Y' or 'N'")
        else:
            return "N"


# Generates all letters in uppercase (if the user wants it)
def generate_upper():
    user_input_upper = input("Would you like to include uppercase (Y/N)? ")

    while True:
        if user_input_upper.upper() == "Y" and len(user_input_upper) == 1:
            return string.ascii_uppercase
        elif user_input_upper.upper() == "Y" and len(user_input_upper) != 1:
            print("You can only do ONE 'Y' or 'N'")
        else:
            return "N"


# Removes any similar characters (if the user wants it)
def remove_similar_characters():
    user_input_exclude_c = input("Would you like to exclude similar characters (Y/N)? ")

    while True:
        if user_input_exclude_c.upper() == "Y" and len(user_input_exclude_c) == 1:
            return "{", "}", "[", "]", "(", ")", "/", "\\", "'", '"', "`", "~", ",", ";", ":", ".", "<", ">"
        elif user_input_exclude_c.upper() == "Y" and len(user_input_exclude_c) != 1:
            print("You can only do ONE 'Y' or 'N'")
        else:
            return "N"


# Removes any ambiguous characters (if the user wants it)
def remove_ambiguous_characters():
    user_input_exclude_a = input("Would you like to exclude ambiguous characters (Y/N)? ")

    while True:
        if user_input_exclude_a.upper() == "Y" and len(user_input_exclude_a) == 1:
            return "Y"
        elif user_input_exclude_a.upper() == "Y" and len(user_input_exclude_a) != 1:
            print("You can only do ONE 'Y' or 'N'")
        else:
            return "N"


# Generates the password by switching between a list and a string
def generate_password(length, symbol, number, lower, upper, exclude_c, exclude_a):
    password = []
    exclude_c = "".join(exclude_c)
    exclude_a = "".join(exclude_a)

    if symbol != "N":
        password.append(symbol)
    if number != "N":
        password.append(number)
    if lower != "N":
        password.append(lower)
    if upper != "N":
        password.append(upper)

    password = "".join(password)

    if exclude_c.upper != "N":
        password = password.replace(exclude_c, "")

    if exclude_a.upper != "N":
        password = "".join(set(password))

    tempList = list(password)
    random.shuffle(tempList)

    password = "".join(tempList)

    new_password = password[:length]

    return new_password


# Outputs the finalized password
def generate_message(password):
    print("Your password is: ", password)

    user_input_message = input("Would you like another password? Y/N? ")

    if user_input_message.upper() == "Y":
        main()


if __name__ == '__main__':
    main()
