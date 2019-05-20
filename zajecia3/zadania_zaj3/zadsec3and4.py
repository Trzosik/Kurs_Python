# inne z sec4 (3)
# Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
# Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
"""
zakres = range(1, 11)
suma = 0
for i in zakres:
    suma = suma + i
    print(suma)

# sec4 (4)
# Napisz program, który wyświetli kolejne wyniki dla silnii liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).
"""
"""
n = int(input("podaj liczbę nie większa niż 8: "))
a = 1
if n < 8:
    for i in range(1, n+1):
        #a *= i
        a = a * i
        print(i, a)
"""
# sec4 zad 6
# Napisz prostą grę, w której użytkownik musi zgadnąć liczbę
# od 0 - 20 ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.


"""
sec_num = 5
for i in range(0, 21):
    a = int(input("podaj liczbę od 0 do 20 : "))
    if a == sec_num:
        print("dobrze!")
        break
    else:
        print("źle! Spróbuj jeszcze raz")
"""

