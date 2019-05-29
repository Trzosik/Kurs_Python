import random


def open_txt(txt):
    with open(txt, 'r') as cytaty:
        lines = cytaty.readlines()
    return lines


def quote_choice():
    lines = open_txt(txt='cytaty.txt')
    generate_quote = random.choice(lines)
    print('Quote for today:\n')
    print('*' * len(generate_quote))
    print(generate_quote.upper())
    print('*' * len(generate_quote))


quote_choice()
