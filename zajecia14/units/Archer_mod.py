from Warrior_mod import Warriors


class Archer(Warriors):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.health = 40
        self.shots = 10

    def attack(self):
        if self.shots == 0:
            print("I am out of shots!")
            return self.shots
        else:
            print(self.name, 'has shot with his bow!')
            self.exp += 0.4
            self.shots = self.shots - 1
            print(self.shots, 'arrows left.')
            return self.shots
