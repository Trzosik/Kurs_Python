# This is the "Hangman" game. Program choose a random word from the implemented list.
# To win user must give the correct word chosen by program. User could give a letter or can guess a whole word.
# There are limited number of attempts which are specified by the user.
# Game could be played solo or with friend.

# modules imported:
import random

# Hello and game mode pick.

print('Welcome to the Hangman game. Please choose your game mode. "solo" or "multi" / multi now unavailable')
# game_mode = input('') DO ZROBIENIA NA KOŃCU

# Word lists for each game mode.

word_list_solo = ['apple', 'university', 'teacher', 'establishment', 'workshop']

# word_multi = input("Please, choose a word and write it down: ")

# Generate random word for solo mode.


def random_word(word_list):
    game_word = random.choice(word_list)
    return game_word


def print_len_game_word(game_word):
    print(len(game_word))


# counter = int(input("How many attempts would you like to have (suggested number: 10): "))


def guess_word():
    generated_word = random_word(word_list_solo)
    print_len_game_word(generated_word)
    user_word = input('Write down word: ')
    if generated_word == user_word:
        print("Good")
    else:
        print("Bad")


guess_word()