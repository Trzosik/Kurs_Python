a = int(input('Jak oceniasz fabułę?'))
b = int(input('Jak oceniasz stylistykę?'))
c = int(input('Jak oceniasz obrazki?'))
sredniaocena = (a + b + c) / 3
if sredniaocena > 7:
    print('Oceniłeś na bardzo dobry')
elif sredniaocena >= 7 <=5:
    print('Oceniłeś przeciętnie')
else:
    print('Oceniłeś słabo')