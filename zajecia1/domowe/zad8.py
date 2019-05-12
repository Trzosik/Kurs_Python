# Zadanie 8
#Ulepsz program z zadania 7, tak aby zwrócił ile banknotów
# 50, 20, 10 i 5 euro otrzyma użytkownik.

print('To jest program do konwersji walut. Proszę podaj jaką kwotę zabierasz na wakację (w PLN): ')
kwotaPLN = float(input())
euro = 4.29
dolar = 3.82
kwotaeuro = int(kwotaPLN / euro)
kwotadolar = int(kwotaPLN / dolar)
banknot50 = int(kwotaeuro / 50)
banknot20 = int(kwotaeuro / 20)
banknot10 = int(kwotaeuro / 10)
bankknot5 = int(kwotaeuro / 5)
print('Na wakacje zabierzesz ', kwotaeuro, 'euro oraz ', kwotadolar, 'dolarów.')
print('W euro otrzymasz ', banknot50, 'banknotów o nominalne 50 euro lub ', banknot20, 'o nominale 20 euro lub', banknot10, 'o nominale 10 euro albo ', bankknot5, 'w nominale 5 euro. Udanych wakacji!')