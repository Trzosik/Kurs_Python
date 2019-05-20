"""

password = input('wpisz swoje hasło')
if len(password) < 7:
    print('złe hasło')
elif password.isalpha():
    print('źle')
elif password.isdigit():
    print('nadal nie')
elif password.islower():
    print('teraz dobrze')
else:
    print('niedobrze')

"""

haslo = input('wpisz haslo')
alfa_num = haslo.isalnum()
not_all_letters = not haslo.isalpha()
not_all_digits = not haslo.isdigit()
correct_alnum = alfa_num and not_all_letters and not_all_digits
one_upper = not haslo.islower() and not haslo.isupper()
correct_len = len(haslo) > 7
if correct_len and correct_alnum and one_upper:
    print('haslo jest git')
else:
    print('popraw haslo')
