# 3▹ Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).


def max_of_two(x, y):
    return x if x > y else y
"""
    if x > y:
        return (x)
    else:
        return (y)
"""

def max_of_three(num1, num2, num3):
    tmp = max_of_two(num1, num2)
    najwieksza = max_of_two(tmp, num3)
    return najwieksza


a = 4
b = 5
c = 3

wieksza = max_of_three(a, b, c)
print(wieksza)
