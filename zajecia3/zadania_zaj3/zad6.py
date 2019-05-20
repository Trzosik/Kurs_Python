lista1 = []
for i in range(4):
    a = input('przedmiot')
    lista1.append(a)
    print(lista1[-1])
    if len(lista1) == 4:
        print('we are ready')
