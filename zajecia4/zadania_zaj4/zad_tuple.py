# 1▹ Utwórz dowolną krotkę, w której elementy mogą się powtarzać. Przekształć ją w set.

"""
krotka1 = (1, 2, 3, 5, 4, 1, 2)
a = set(krotka1)
print(a)
"""

"""
# 2▹ Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}. Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?

L_test = [1, 2, 3, 4]
T_test = (1, 2, 3, 4)
S_test = {1, 2, 3, 4}
# metody indeksujące, remove, etc

"""

# 3▹ Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki, a oraz nieparzystych elementów z drugiej.

"""

krotka_1 = ("coś", "coś2", "coś3", "coś4")
krotka_2 = ("ktoś1", "ktoś2", "ktoś3", "ktoś4")
lista_krotki1 = list(krotka_1)
lista_krotki2 = list(krotka_2)
# slicing [od, do, co który]
a = lista_krotki1[0::2]
b = lista_krotki2[1::2]
c = a + b
print(c)

"""

a = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
a1 = a[0::3]
a2 = a[1::3]
a3 = a[2::3]
b1 = a1.reverse()
b2 = a2.reverse()
b3 = a3.reverse()
print(b1, b2, b3)


