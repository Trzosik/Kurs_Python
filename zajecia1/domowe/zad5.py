# Zadanie 5
# Napisz program, który pyta użytkownika o 2 liczby
# a następnie dzieli jedna przez drugą.
# Pokaż ile razy pierwsza liczba mieści się w drugiej
# oraz jaka jest reszta tego dzielenia.
liczba1 = float(input('Podaj pierwszą liczbę: '))
liczba2 = float(input('Podaj drugą liczbę: '))
obliczenie1 = liczba1 / liczba2
obliczenie2 = int(liczba2 / liczba1)
obliczenie3 = int(liczba2 % liczba1)
print('Liczba pierwsza mieści się w drugiej ', obliczenie2, 'razy. Zaś reszta z dzielenia wynosi: ', obliczenie3)
