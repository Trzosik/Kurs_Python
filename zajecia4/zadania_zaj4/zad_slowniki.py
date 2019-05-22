"""
my_dict = {
  'apple': 'jablko',
  'ball': 'pilka',
  'umbrella': 'parasolka'
  }

a = my_dict
pusta = []
print(pusta.fromkeys([1, 2, 3], "aka")
print("apple" in a)
print(a.keys())
print(a.values())
print(a.items())

"""

"""

lists_to_dict = [[1, "a"], [2, "b"]]
dict_from_list = dict(lists_to_dict)
print(dict_from_list)

"""

"""
tuples_to_dict = ((3, "c"), (4, "d"))
dict_from_tuples = dict(tuples_to_dict)
print(dict_from_tuples)

"""

"""

n = int(input("Wprowadź liczbę naturalną: "))

tab = [["-"] * n] * n

for j in tab:
    print(" ".join(j))

"""





wierszyk = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""
pusty_dict = {}
a = wierszyk.lower()
b = a.replace(",", "")
c = b.split()
for i in c:
    if i in pusty_dict:
        pusty_dict[i] += 1
    else:
        pusty_dict[i] = 1
print(pusty_dict)

for key, value in pusty_dict.items():
    print(key, "\t", value)
