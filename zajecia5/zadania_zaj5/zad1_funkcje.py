# zadania z dnia 22 05 2019

"""

def mood():
    print("How are you?")

mood()

"""

"""

def my_mood(answear):
    print("My mood today:")
    print(answear)

resp = input("How are you?")
my_mood(resp)

"""

"""

def my_mood(answear):
    return answear * 2

resp = input("Howdy?!")
twiced = my_mood(resp)
print("My mood is like", twiced)

"""

# zadanie ćwiczeniowe: pobiera dane o ksiazce i uzupelnia biblioteke, nastepnie wyszukuje ksiazke i w razie bledu podaje komunikat


def pobierz_dane():
    biblioteka = {}
    ile = int(input("Ile książek:"))
    for i in range(ile):
        tytul = input("Podaj nazwę książki:")
        ocena = int(input("Podaj ocenę książki w skali od 1 do 10:"))
        biblioteka[tytul] = ocena
    return biblioteka

def znajdz_ksiazke(tytul):
    print("Ocena wybranej książki to:", bibl[tytul])

bibl = pobierz_dane()
ksiazka = input("Ocenę jakiej książki chcesz sprawdzic?")


if ksiazka in bibl:
    znajdz_ksiazke(ksiazka)
else:
    print("nie ma")
