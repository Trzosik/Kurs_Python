# Zadanie 7
# Napisz konwerter walut.
# Program poprosi użytkownika o kwotę pieniędzy, jaką wezmą na wakacje
# a następnie przeliczy tę kwotę w euro oraz w dolarach.
# Zignoruj wszelkie centy, które mogą wyniknąć z konwersji.
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

print('To jest program do konwersji walut. Proszę podaj jaką kwotę zabierasz na wakację (w PLN): ')
kwotaPLN = float(input())
euro = 4.29
dolar = 3.82
kwotaeuro = int(kwotaPLN / euro)
kwotadolar = int(kwotaPLN / dolar)
print('Na wakacje zabierzesz ', kwotaeuro, 'euro oraz ', kwotadolar, 'dolarów.')
