'''
filename = 'tekst.txt'
with open(filename, 'r') as new_tekst:
    content = new_tekst.read()
    print(content)
'''
'''
with open('tekst.txt', 'r') as fopen:
    for line in fopen:
        print('--', line)
'''
'''
with open('tekst.txt', 'r') as fopen:
    while True:
        current_line = fopen.readline()

    # aktualna linia jest pusta
        if current_line == '':
      # dotarlismy do konca
            break
        print(current_line)
'''
'''
with open('tekst.txt', 'r') as fopen:
    print(fopen.readlines())
'''
'''
with open('tekst.txt', 'r') as fopen:
    lines = fopen.readlines()
for i in lines:
    print('*', i)
'''
with open('save.txt', 'w') as f:
    f.write('Line1\n')
    f.write("Line2\n")
