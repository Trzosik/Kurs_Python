# 7▹ Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
# Co wiemy o tych numerach tych kart?
#    All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
#    MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
#    American Express card numbers start with 34 or 37 and have 15 digits.

number = input("Podaj nr karty")
# błąd numeru
len_of_number = len(number)
if len_of_number not in [13, 15, 16]:
    print("Nieistnieje taka karta")
else:
    reszta kodu

# czy jest visa
def is_visa(number):
    if len_of_number not in [13, 16]:
        return False
    else:
        if number[0] == "4":
            return True
        else:
            return False


# czy jest master
def is_master(number):
    if len_of_number != 16:
        return False
    else:
        if int(number[:2]) >= 51 and int(number[:2]) <= 55:
            return True
        elif 2221 >= int(number:4) and <= 2720:
            return True
        else:
            return False



# czy jest american
