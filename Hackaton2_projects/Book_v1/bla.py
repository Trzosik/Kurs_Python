class Bla:
    def __init__(self, name, last):
        self.name = name
        self.last = last

    def show(self):
        print(self.name, self.last)


a = Bla('A', 'Aaa')
b = Bla('B', 'bbb')

lista = [a, b]

for i in lista:
    i.show()