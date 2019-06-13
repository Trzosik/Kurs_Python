"""
FIFO Queue implementation. Class FIFO has atribute list; shows list, add to and pop from the list.
"""


class FIFO:
    def __init__(self, kolejka):
        self.kolejka = kolejka

    def show_kolejka(self):
        print(*self.kolejka)

    def check_if_lista_empty(self):
        if not self.kolejka:
            print('Lista jest pusta')
        else:
            print('Lista istnieje')

    def put_element_into(self):
        element = input('Podaj element')
        self.kolejka.append(element)

    def delete_element_from(self):
        self.kolejka.pop(0)


random_kolejka = FIFO(['a', 'b', 'c'])

random_kolejka.check_if_lista_empty()

random_kolejka.put_element_into()

random_kolejka.delete_element_from()

random_kolejka.show_kolejka()
