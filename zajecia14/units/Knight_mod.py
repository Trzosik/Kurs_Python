from Warrior_mod import Warriors


class Knight(Warriors):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.health = 60

    def attack(self):
        print(self.name, 'has attacked with his sword!')
        self.exp += 0.3
