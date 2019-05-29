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


def quote_choice2():
    lines = open_txt(txt='cytaty.txt')
    quotes = []
    for i in range(3):
        generate_quote = random.choice(lines)
        quotes.append(generate_quote)
    print('Quote for today:\n')
    for i in quotes:
        print('*' * len(i))
        print(i.upper())
        print('*' * len(i))


quote_choice2()
