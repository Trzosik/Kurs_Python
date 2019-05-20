"""
zmienna1 = input('tu wpisz slowo: ')
zmienna2 = int(len(zmienna1)/2)
zmienna3 = zmienna1[zmienna2 -1] + zmienna1[zmienna2] + zmienna1[zmienna2 + 1]
print(zmienna3)
"""

"""
s1 = input('tu cos wpisz')
s2 = input('tu cos tez wpisz')
polowa = len(s1)//2
s3 = s1[:polowa] + s2 + s1[polowa]:
print(s3)
"""

"""
quote = 'Honesty is the first chapter in the book of wisdom.'
print(len(quote))
print(quote[-7:])
"""

"""
quote = 'Honesty is the first chapter in the book of wisdom.'
polowa = len(quote)//2
print(quote[0:polowa])
print(quote[-1])
print(quote[polowa::3])
print(quote[::2])
print(quote[::-1])
quote2 = quote.replace('wisdom', 'friendship')
print(quote2)
"""

"""
print('Pytamy o książkę')
tytul = input('Tu wpisz tytuł książki: ')
nazwisko = input('Tu wpisz nazwisko autora: ')
strony = int(input('Tu wpisz liczbe stron: '))
"""

# Palindrom

palindrom1 = input('Tu wpisz swój palindrom: ')
if palindrom1 == palindrom1[::-1]:
    print(True)
else:
    print(False)

# zadanie na kod genetyczny z flynerd https://www.flynerd.pl/2018/01/python-metody-typu-string.html
