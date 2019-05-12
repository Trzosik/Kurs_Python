# Zadanie 4
# Napisz skrypt, który zapyta użytkownika o trzy liczby całkowite,
# a następnie pomnóż dwa pierwsze. przed podzieleniem wyniku przez trzecią liczbę. 
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.
print("------------------ Symulacje liczb ------------------")
print("Program pyta użytkownika o 3 dowolne liczby całkowite")
print("a następnie zwraca ich symulację.")
print()
a = int(input('Wprowadź pierwszą liczbę '))
b = int(input('Wprowadź drugą liczbę '))
c = int(input('Wprowadź trzecią liczbę '))
obliczenie1 = a * b
obliczenie2 = obliczenie1 / c
print('Symulacja Twoich liczb daje wynik: ', obliczenie2)
