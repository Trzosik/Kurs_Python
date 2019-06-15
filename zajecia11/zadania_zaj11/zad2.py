class Dog:
    def __init__(self, name, color, race, barking_type):
        self.name = name
        self.color = color
        self.race = race
        self.barking_type = barking_type

    def bark(self):
        print(self.barking_type)

    def wave(self):
        print('...===...')


Jamnik_Stefan = Dog('Stefan', 'White', 'Jamnik', 'Hauuuuu')

Jamnik_Stefan.bark()
Jamnik_Stefan.wave()

print(Jamnik_Stefan)