# dane są tuple dla każdego miesiąca, zadanie - wyświetlić każdy, miesiąc, przyjmujemy tydzień jako 7 dniowy

month_tuple_data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]
"""
def stworz_miesiac():
    for i in month_tuple_data:
        miesiac_name = i[0]
        dni = i[1]
        miesiac = [miesiac_name, dni]
        lista_miesiecy = []
        lista_miesiecy.append(miesiac)
"""

def czy_dzien_dwucyfrowy(dzien):
    if dzien < 10:
        str(dzien)
        print("0"dzien)
    else:
        print(dzien)


def printuj_miesiac_dni(mies_ldni):
    print(mies_ldni[0])
    for i in mies_ldni[1]:
        print(i, end=' ')
        if (i + 1) % 7 == 0:
            print()



def printuj_kalendarz():
    for j in month_tuple_data:
        print()
        printuj_miesiac_dni(j)
        print()


printuj_kalendarz()
