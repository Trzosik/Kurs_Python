# This is the "Hangman" game by Adrian Trzoss. Program choose a random word from the implemented list.
# To win user must give the correct word chosen by program. User could give a letter or can guess a whole word.
# There are limited number of attempts which are specified by the user.
# Game could be played solo or with friend.

# modules imported:
import random

# Hello and game mode pick.

print('Welcome to the Hangman game. Please choose your game mode. Type "Single" or "Multi" / multi now unavailable')
# game_mode = input('') TO DO LATER

# Word lists for each game mode.

word_list_solo = ['apple', 'university', 'teacher', 'establishment', 'workshop']

# word_multi = input("Please, choose a word and write it down: ") TO DO LATER

# Function: Generate random game_word for solo mode from the word_list_solo.


def random_word(word_list):
    game_word = random.choice(word_list)
    return game_word


# Function: full_guess asks User to guess the game_word. If True User wins the game, else try again.


def full_guess(generated_word):
    user_word = input('Write down word: ')
    user_word = user_word.lower()
    if generated_word == user_word:
        print("Good. You have won!")
        return True
    else:
        print('Bad. Try again.')
        return False


# Function: letter_guess asks User for a letter. If letter is in game_word informs and adds (later in main function) to
# guessed letters list. Same for wrong letter. Return both.


def letter_guess(generated_word):
    letter = input('Give a letter:')
    letter = letter.lower()
    good_letter = '-'
    bad_letter = '-'
    if letter in generated_word:
        print('Good. You guessed a letter!')
        good_letter = letter
    else:
        print('Wrong letter!.')
        bad_letter = letter
    return good_letter, bad_letter


# Function: fill letters takes empty word, list of guessed letters and game word from main_function.
# Function chekcs if elements in the list of guessed letters are in game word; then fill empty word with these letters.
# Returns new empty word with filled letters.


def fill_letters(generated_word, list_guessed_letters, empty_word):
    new_empty_word = empty_word
    for i in range(0, len(generated_word)):
        if generated_word[i] in list_guessed_letters:
            new_empty_word = new_empty_word[:i] + generated_word[i] + new_empty_word[i + 1:]
    return new_empty_word


# Function MAIN: Main launches and manages the program. First it generates random game word.
# Secondly, it creates empty word which will later show guessed letters in correct order.
# Function prints the word length as a tip. Also game has a limited number of attempts == 5.
# Creates two lists which are supposed to be updated with good/wrong letters (as a reminder and for fill_letters)
# In while function each time asks for the User decision, whether to make final guess or to pick a letter.
# If final guess then main goes to full_guess function. Upon return depends on if User wins or has to try again.
# After full_guess counter will subtract one attempt. Then return to the decision module split.
# If in decision User chose other then 'Yes' function uses letter guess module. As an effect it adds returns to lists.
# After module letter guess User loses one attempt. Then function informs about the result in the given info text.
# After informing User about list of letters program goes to fill letters which will replace "unknown mark" (*) with
# letters from guessed letters list and will print the new word as a hint. If counter goes to zero User loses the game.


def main_function():
    generated_word = random_word(word_list_solo)
    empty_word = '*' * int(len(generated_word))
    print('Word length is', len(generated_word))
    counter_games = 5
    list_guessed_letters = []
    list_wrong_letters = []
    while counter_games > 0:
        print('You have', counter_games, 'attempts.')
        decision = input("Would you like to make final guess? Yes/No: ")
        if decision.lower() == 'yes':
            answer = full_guess(generated_word)
            if answer is True:
                break
            else:
                counter_games = counter_games - 1
                continue
        else:
            good, wrong = letter_guess(generated_word)
            if good.isalpha():
                list_guessed_letters.append(good)
            if wrong.isalpha():
                list_wrong_letters.append(wrong)
        counter_games = counter_games - 1
        print('Guessed letters:', list_guessed_letters, 'Wrong letters:', list_wrong_letters)
        new_empty_word = fill_letters(generated_word, list_guessed_letters, empty_word)
        empty_word = new_empty_word
        print(empty_word)
    if counter_games == 0:
        print()
        print('Sorry, You have lost the game.')
    print()
    print('Endgame.')


# Let's play the game!

main_function()
