# funkcja search email
'''


def search_email():
    user_email = input('podaj maila')
    email_list = ['siema', 'co', 'kot']
    for i in range(len(email_list)):
        if user_email == email_list[i]:
            print(i)
            break
    return i


search_email()
'''
'''
'dom' = 0
'szkola' = 1
'kosciol' = 2
'bar' = 3
'szpital' = 4
'kino' = 5
'teatr' = 6
'''
'''
lista = {
        0: [1, 2, 3],
        1: [0, 4],
        2: [0, 3, 5],
        3: [0, 2, 4],
        4: [1, 3, 5, 6],
        5: [2, 4, 6],
        6: [4, 5]
         }


for key, value in lista.items():
    for i in value:
        print(key, "---", i)
'''


def wypisz(n):
    if n < 0:
        print("nic")
        n = -n
