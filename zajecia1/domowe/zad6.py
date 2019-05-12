# Zadanie 6
# Zarówno lodówka, jak i winda mają wysokość, szerokość i głębokość. 
# Dowiedz się, ile miejsca pozostało w windzie, gdy lodówka jest w środku.
# Załóżmy, że wymiary lodówki zawsze będą mniejsze niż windy ( jest to prawdopodobne?)
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

print('To jest kalkulator windo-lodówek. Fun fact na dziś: dowiedz się ile miejsca pozostanie w windzie po upchnięciu w niej lodówki. W tym celu podaj wymiary obu.')
print()
winda1 = []
windaS = int(input('Podaj wysokość windy w centymetrach: '))
windaW = int(input('Podaj szerokość windy w centymetrach: '))
windaG = int(input('Podaj głębokość windy w centymetrach: '))
lodowka1 = []
lodowkaS = int(input('Podaj wysokość lodówki w centymetrach: '))
lodowkaW = int(input('Podaj szerokość lodówki w centymetrach: '))
lodowkaG = int(input('Podaj głębokość lodówki w centymetrach: '))
winda1.append(windaS)
winda1.append(windaW)
winda1.append(windaG)
lodowka1.append(lodowkaS)
lodowka1.append(lodowkaW)
lodowka1.append(lodowkaG)
objetoscwindy = winda1[0] * winda1[1] * winda1[2]
objetosclodowki = lodowka1[0] * lodowka1[1] * lodowka1[2]
wolne = objetoscwindy - objetosclodowki
print('W windzie pozostało ', wolne, 'cm sześciennych')
