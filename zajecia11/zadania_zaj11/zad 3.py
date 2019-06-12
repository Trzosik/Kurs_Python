"""3▹ Stwórz własną implementację kolejki FIFO. Klasa Kolejka powinna na starcie przyjmować listę elementów.
Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki, sprawdzenie czy jest pusta, dodanie elementu do kolejki (put),
wyjęcie elementu z kolejki (get).

Utwórz kilka obiektów klasyz różnymi parametrami.
"""


class FIFO:
    def __init__(self, lista_kolejkowa):
        self.lista_kolejkowa = lista_kolejkowa

    def show_lista_kolejkowa(self):
        print(self.lista_kolejkowa)
#
#     def check_if_lista_void(self):
#         if not self.lista_kolejkowa:
#             print('Lista jest pusta')
#
#     def put_element_into(self):
#         element = input('Podaj element')
#         self.lista_kolejkowa = self.lista_kolejkowa.append(element)
#         return self

    def get_element_from(self):
        return self.lista_kolejkowa.pop(0)


random1 = FIFO(['a', 'b', 'c'])

print(random1)

# random1.show_lista_kolejkowa()
#
# random1.put_element_into()

random1.get_element_from()

random1.show_lista_kolejkowa()