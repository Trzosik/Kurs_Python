# Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
#
# Co wiemy o tych numerach tych kart?
# All Visa card numbers start with a 4.
# New cards have 16 digits. Old cards have 13.

# MasterCard numbers either start with the numbers 51 through 55
# or with the numbers 2221 through 2720. All have 16 digits.

# American Express card numbers start with 34 or 37 and have 15 digits.
#
with open('cards_numbers.txt', 'r') as cards_file:
    numbers = cards_file.readlines()


def is_visa(number):
    if len_of_number not in [13, 16]:
        return False
    else:
        if number[0] == '4':
            return True
        else:
            return False


def is_mastercard(number):
    if len_of_number != 16:
        return False
    else:
        if 51 <= int(number[:2]) <= 55:
            return True
        elif 2221 <= int(number[:4]) <= 2720:
            return True
        else:
            return False


def is_american_express(number):
    if len_of_number != 15:
        return False
    else:
        if number[:2] == '34' or number[:2] == '37':
            return True
        else:
            return False


def save_to_file(card_type, number):
    save_file = card_type + '.txt'
    with open(save_file, 'a+') as sf:
        sf.write(number + '\n')


def check_card_type(number):
    # czy visa
    if is_visa(number):
        print("to visa")
        save_to_file('visa', number)
    # czy jest master
    elif is_mastercard(number):
        print("to mastercard")
        save_to_file('mastercard', number)
    # czy american
    elif is_american_express(number):
        print("yay american express to jeszcze istnieje?")
        save_to_file('american', number)
    else:
        print("nie znam twojej karty")


# number = input("Podaj nr karty: ")

# czy numer jest bledny
# len_of_number = len(number)

# if len_of_number not in [13, 15, 16]:
#    print("Dlugosc nieprawidlowa")

# check_card_type(number)
len_of_number = 0
for num in numbers:
    num = num.replace('\n', '')
    len_of_number = len(num)
    check_card_type(num)

