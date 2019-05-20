"""
lista3x3 = [
[1, 0, 0],
[0, 1, 0],
[0, 0, 1],
]

print(lista3x3)

[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
for i in lista3x3:
    print(i)

[1, 0, 0]
[0, 1, 0]
[0, 0, 1]

print(lista3x3[1][1])

"""

"""
# 1▹ Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry. Elementy na liście posortuj alfabetycznie, a następnie wyświetl.

lista = ["plecak", "buty", "kijki", "czapka", "latarka"]
lista.sort()
print(lista)

"""




"""
# 3 Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

a = []
for i in range(0, 5):
    lista = (input("Podaj liczby: "))
    a.append(lista)

if a[0] == a[-1]:
    print("True")
else:
    print("False")
"""

# 5▹ Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
#
#     Dorota, Wellman, dziennikarka
#
#     Adam, Małysz, sportowiec
#
#     Robert, Lewandowski, piłkarz
#
#     Krystyna, Janda, aktorka
#
# Wyświetl w sposób przyjazny dla użytkownika
"""
people = [
    ["dorota", "w", "dz"],
    ["adam", "m", "sp"],
    ["robert", "l", "pil"]
]
for i in people:
    print("*".join(i))
"""

"""
tablica_pusta = []
for i in range(3):
    name = input("podaj imię, ")
    surname = input("podaj nazwisko")
    job = input("podaj zawod")
    tablica_pusta.append([name, surname, job])
for j in tablica_pusta:
    print("\t".join(j))
"""

