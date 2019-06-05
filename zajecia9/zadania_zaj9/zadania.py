# 1▹ Stwórz listę składającą się z kilku elementów różnego typu. W pętli spróbuj wykonać dzielenie 10 przez wartość z listy. Złap wyjątki jakie mogą się przy tej okazji wydarzyć.
'''
lista = ['a', 50, 25.4, 'baba', 14.75, '5as5', 0, 440, 6600, 'ala', {}, (), {'cos': 1}]
for i in lista:
    try:
        wynik = i / 10
        wynik2 = int(i)
        print(wynik)
        print(wynik2)
    except (ZeroDivisionError, ValueError, TypeError) as error:
        print(error)
'''
# 2▹ Utwórz dowolną krotkę zawierającą kilka wartości np. 10. Pozwól użytkownikowi podać dowolny index oraz wartość.
# Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd


import sys

krotka = ('imie', 'nazwisko', '02.07.1992', 'miejsce', '176', '65.0')


def function1():
    try:
        index = int(input("Podaj indeks"))
        wartosc = input("podaj wartosc")
        return index, wartosc
    except (TypeError, ValueError):
        print("ojojoj", sys.exc_info()[0])
        index = int(input("Podaj LICZBĘ!"))
        return index, wartosc


def function2(index, wartosc):
    try:
        krotka[index] = wartosc
        print(krotka[index])
    except (TypeError, ValueError):
        print("ojojoj", sys.exc_info()[0])
        lista_od_krotki = list(krotka)
        lista_od_krotki[index] = wartosc
        print(lista_od_krotki[index])
        new = lista_od_krotki
        print("nowa", new)


def main():
    a, b = function1()
    function2(a, b)
    print('udalo sie')


if __name__ == '__main__':
    main()
