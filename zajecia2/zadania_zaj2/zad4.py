# Zadanie 7
# Stwórz dwie dowolne zmienne przechowujące wartość liczbową i tekstową.
# Użyj funkcji format(), by wyświetlić zdanie zawierające te wartości.

a = int(input("Tu podaj liczbę: "))
b = str(input("Tu podaj tekst: "))
c = "tu jest jakieś zdanie {0} {1}"
print(c.format(a, b))

