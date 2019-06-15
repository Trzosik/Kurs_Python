# Phone_book v1

import json


def start_new_book():
    phone_book = []
    print(phone_book)
    return phone_book


def save_to_file(phone_book):
    filename = input('Podaj nazwe pliku do zapisu')
    filename = filename + '.json'
    print(filename)
    with open(filename, 'w+') as f:
        json.dump(phone_book, f)


def create_new_wpis(phone_book):
    nowe_imie = input('Podaj nowe imie')
    nowy_numer = input('Podaj numer')
    try:
        nowy_numer = int(nowy_numer)
    except ValueError:
        print('Błąd!')
    else:
        nowe_imie = ('imie', nowe_imie)
        nowy_numer = ('numer', nowy_numer)
        nowy_wpis = (nowe_imie, nowy_numer)
        nowy_wpis = dict(nowy_wpis)
        phone_book.append(nowy_wpis)
        print(nowy_wpis)
        return phone_book


def load_phone_book():
    filename = input('Podaj nazwe pliku do wczytania')
    filename = filename + '.json'
    print(filename)
    try:
        with open(filename, 'r+') as f:
            phone_book = json.load(f)
            print(phone_book)
            return phone_book
    except FileNotFoundError:
        print('Nie ma takiego pliku')


def length(phone_book):
    length_phone_book = len(phone_book)
    print(length_phone_book)


def find_wpis(phone_book):
    check_imie = input('Podaj imie')
    print(check_imie)
    for i in range(len(phone_book)):
        if check_imie in phone_book[i].values():
            print(phone_book[i])
    # want_to_edit = input('Do you want to edit? y/n')
    # if want_to_edit == 'y':
    #
    # else:
    #     return None


def main():
    phone_book = []
    while True:
        print('Press 1:', 'to Load_phone_book')
        print('Press 2:', 'to start new phonebook')
        print('Press 3:', 'to Save_to_file')
        print('Press 4:', 'to Create_new_wpis')
        print('Press 5:', 'to check Length')
        print('Press 6:', 'to print Phone_book')
        print('Press 7:', 'to find wpis')
        print('Press 0:', 'to Exit')
        press = int(input('Press the button'))
        if press == 1:
            phone_book = load_phone_book()
        elif press == 2:
            phone_book = start_new_book()
        elif press == 3:
            save_to_file(phone_book)
        elif press == 4:
            create_new_wpis(phone_book)
        elif press == 5:
            length(phone_book)
        elif press == 6:
            for i in range(len(phone_book)):
                print([i])
                for key, value in phone_book[i].items():
                    print('{} : {}'.format(key, value))
                print()
        elif press == 7:
            find_wpis(phone_book)
        elif press == 0:
            print("It's the little differences...")
            break
        else:
            print("Nonavailable")


if __name__ == "__main__":
    main()
