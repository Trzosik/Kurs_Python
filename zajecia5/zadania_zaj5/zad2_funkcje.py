# zadania ze strony co do funkcji (przed zmiennymi 1 -4)
# wzór na pole koła PI r **
"""
def pole_kola():
    r = float(input("Podaj promień koła w cm:"))
    pi = 3.14
    wzor = pi * (r**2)
    return wzor

Wynik = pole_kola()
print(Wynik)
"""

# zad 2 czy podana liczba jest parzysta
"""
def czy_parzysta():
    user_num = float(input("Podaj liczbę: "))
    if user_num % 2 == 0:
        print("Liczba jest parzysta")
    else:
        print("Liczba jest nieparzysta")

podaj_liczbe = czy_parzysta()
"""

# zad 3 Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.
"""
def suma_liczb():
    lista_liczb = []
    ile_pobrac = int(input("Podaj ile liczb zamierzasz wpisac na listę:"))
    for i in range(ile_pobrac):
        user_num = int(input("Podaj liczbe:"))
        lista_liczb.append(user_num)
    print(lista_liczb)
    wynik = sum(lista_liczb)
    print(wynik)

test1 = suma_liczb()
"""
# 4▹ Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)

def czy_parzysta(num):
    if user_num % 2 == 0:
        print("Liczba jest parzysta")
    else:
        print("Liczba jest nieparzysta")
# user_num = float(input("Podaj liczbę: "))
# czy_parzysta(user_num)


def wypisz_parzyste():
    lista_liczb = []
    ile_pobrac = int(input("Podaj ile liczb zamierzasz wpisac na listę:"))
    for i in range(ile_pobrac):
        user_number = int(input("Podaj liczbe:"))
        lista_liczb.append(user_number)
    print(lista_liczb)
    dlugosc_listy = len(lista_liczb)
    for j in range(dlugosc_listy):
        czy_parzysta(lista_liczb[j])
        print(j)

        
x = wypisz_parzyste()
