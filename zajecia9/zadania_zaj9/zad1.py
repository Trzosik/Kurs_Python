import sys
'''

try:
    x = 5 / 0
except ZeroDivisionError as e:
    print("Pamiętaj kolego nie dziel przez zero! Twój wyjątek to:", e)
    x = 0


print(ZeroDivisionError.__bases__)


try:
    5 / 0
except ArithmeticError:
    print("Got arithmetic error")

'''
'''
random_list = ['a', 0, 2, 5, 6]

for value in random_list:
    try:
        print('Wartość: ', value)
        r = 1/int(value)
        break
    except (ValueError, ZeroDivisionError) as error:
        print('Oops! Wystąpił błąd: ', error)
        print('Następna wartość')
        print()


print('Dzielenie przez', value, 'wynosi', r)
'''


def predict_future():
  num = int(input("Podaj dowolną liczbę naturalną: "))
  if num < 0:
    raise ValueError("To nie jest liczba naturalna!")
  else:
    print("Za", 10 * num, "ludzkość będzie mogła się teleportować")


try:
  predict_future()
except Exception as e:
    print(e)
