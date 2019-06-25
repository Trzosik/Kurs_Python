from units.Archer_mod import Archer
from units.Knight_mod import Knight


def main():
    # Mateusz = Knight('Mateusz')
    # print(Mateusz)
    # Mateusz.march(100)
    # print(Mateusz)
    # Mateusz.attack()
    # print(Mateusz)
    #
    # Kajtek = Archer('Kajtek')
    # print(Kajtek)
    # Kajtek.march(200)
    # print(Kajtek)
    # Kajtek.attack()
    # print(Kajtek)

    lista_knights = []
    for i in range(0, 4):
        i = Knight(i)
        lista_knights.append(i)
    print(lista_knights)

    for j in lista_knights:
        j.march(1000)
        j.attack()
    print(lista_knights)

    lista_archers = []
    for m in range(0, 3):
        m = Archer(m)
        lista_archers.append(m)
    print(lista_archers)

    for n in lista_archers:
        n.march(200)
        m.attack()
    print(lista_archers)

    army = lista_archers + lista_knights
    print(army)
    for x in army:
        x.attack()
    print(army)


if __name__ == '__main__':
    main()
