# suma naturalnych

"""
zakres = range(1, 11)
suma = 0
for i in zakres:
    suma = suma + i
    print(suma)
"""

# celsjusz to fahrenheit

start = 0
limit = 200
step = 20
fahr = start
while (fahr <= limit):
    C = 5 / 9 * (fahr - 32)
    print(fahr, '\t', C)
    fahr = fahr + step