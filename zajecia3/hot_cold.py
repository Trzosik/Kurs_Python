# Zadanie 11
# Stwórz grę ciepło zimno.
# Komputer losuje liczbę z zakresu od 1 do 100.
# Użytkownik podaje swój traf.
# Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# Jeśli użytkownik zgadnie wygrywa gracz.
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

import random
print("Witaj w grze ciepło/zimno!")
a = random.randint(0, 101)
token = 6
d = 0 # jakaś tam pomocznicza zmienna w sumie
for i in range(1, 7):
    b = int(input("Podaj liczbę od 1 do 100: "))
    if a == b:
        print("Brawo! Zgadłeś! Jesteś diamentem!")
        break
    else:
        c = token - i
        if a - b < 0:
            d = b - a
            if d > 10:
                print("Słabo i zimno jak w Kieleckim, (wyszła liczba ujemna próbuj dalej), masz jeszcze", c, "prób")
            else:
                print("Blisko! Ciepło jak w Chałupach latem, spróbuj jeszcze raz, (wyszła liczba ujemna), możesz spróbować", c, "razy")
        elif a - b > 10:
            print("Ale słabo...zimno! Spróbuj jeszcze raz (wyszła liczba dodatnia)! Zostało Ci:", c, "podejść")
        else:
            print("Ciepło! Spróbuj jeszcze raz! (wyszła dodatnia) Zostało Ci:", c, "podejść")
print("Koniec Gry. Liczba to: ", a)
# pętla pierwsza - trafiłeś; pętla druga - sprawdź wynik różnicy (dodatni / ujemny) i w zależności od różnicy czy większy czy mniejszy niż 10, podaj komunikat & re-run / a na końcu pełni funkcje testową