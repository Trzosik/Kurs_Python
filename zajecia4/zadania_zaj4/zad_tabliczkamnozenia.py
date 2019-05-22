# Tabliczka mnożenia 10 x 10 (lista wiersz * lista kolumna = lista wynik)

wyniki = []

for i in range(1, 11):
    for j in range(1, 11):
        a = int(i * j)
        wyniki.append(a)

    print(wyniki)
