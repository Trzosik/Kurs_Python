class Warriors:

    def __init__(self):
        self.health = 60
        self.exp = 0

    def __repr__(self):
        return 'Warrior: health = {} , exp = {}'.format(self.health, self.exp)

    def march(self, distance):
        print('Warrior: I walked for', distance, 'meters')


class Knight(Warriors):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.health = 60

    def march(self, distance):
        # super().march(distance)
        print(self.name, ': I walked for', distance, 'metersXXX')
        self.exp = self.exp + (distance * 0.2)
        return self.exp

    def attack(self):
        print(self.name, 'has attacked with his sword!')
        self.exp += 0.3


class Archer(Warriors):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.health = 40
        self.shots = 10

    def __repr__(self):
        return self.name, ': health = {} , exp = {}'.format(self.health, self.exp)

    def march(self, distance):
        print(self.name, ': I walked for', distance, 'meters')
        self.exp = self.exp + (distance * 0.2)
        return self.exp

    def attack(self):
        if self.shots == 0:
            print("I am out of shots!")
            return self.shots
        else:
            print(self.name, 'has shot with his bow!')
            self.exp += 0.4
            self.shots = self.shots - 1
            print(self.shots)
            return self.shots


def main():
    Mateusz = Knight('Mateusz')
    Mateusz.__repr__()
    Mateusz.march(100)
    Mateusz.attack()
    Mateusz.__repr__()

    # Kajtek = Archer('Kajtek')
    # Kajtek.__repr__()
    # Kajtek.march(100)
    # Kajtek.attack()
    # Kajtek.__repr__()


if __name__ == '__main__':
    main()
