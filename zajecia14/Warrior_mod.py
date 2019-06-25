class Warriors:

    def __init__(self):
        self.exp = 0

    def __repr__(self):
        class_name = self.__class__.__name__
        return '{}: health = {} , exp = {}'.format(class_name, self.health, self.exp)

    def march(self, distance):
        class_name = self.__class__.__name__
        print(class_name, ': I walked for', distance, 'meters')
        self.exp += 0.2 * distance


print('Base Class - Warrior')
