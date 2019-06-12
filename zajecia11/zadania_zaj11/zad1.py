"""
book = {
    'title': 'Granica',
    'author': 'Zofia Nalkowska',
    'year': '1879',
    'pages': '210',
    'time': '420'
}

print(book['title'])
"""

"""
a.title = 'Pan Tadeusz'
a.author = 'Adam Mickiewicz'
a.hero = 'Tadeusz Soplica'
a.location = 'Soplicowo'
a.more_than_100 = True

b = Book()

b.title = 'Ilustrowany przewodnik po algorytmach'
b.author = 'XYZ'
b.hero = 'Mouse'

print(a.hero)
"""


class Book:

    has_cover = True

    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def show(self):
        print('{}, {}, {}'.format(self.title, self.author, self.year))

    def get_read_time(self):
        time_in_hours = int(self.pages * 2.5 // 60)
        minutes_left = int(self.pages * 2.5 % 60)
        return str(time_in_hours) + ':' + str(minutes_left)


ksiazka1 = Book('Granica', 'Zofia', '1935', 210)
ksiazka2 = Book('Lalka', 'Prus', '1880', 430)

ksiazka1.show()
t = ksiazka1.get_read_time()
t2 = Book.get_read_time(ksiazka2)
print(t)
print()
print(t2)
print()

a = 'Abrakadabra'
print(a)
print(a.upper())
print(a.lower())
print(type(a))
print(type(ksiazka1))
