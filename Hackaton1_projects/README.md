# This is the "Hangman" game by Adrian Trzoss. Program chooses a random word from the implemented list and User tries to guess that word within 5 attempts.

# Contents:

1. Project Summary:
	a) Introduction
	b) Game rules
	c) Used technology and methods
2. Setup
3. Algorithm step by step
4. Known issues
5. Info about contributor

# 1. Project Summary:

	# a) Introduction
		The Hangman game by Adrian Trzoss is a new version of well-known classic Hangman game implemented with Python programming language. Game was developed by the author as a part of his Python programming language course by Code:me in spring 2019. Current version: 1.0 Beta.

	# b) Game rules
		In order to win User must give the correct word chosen by program. User could give a letter or can guess a whole word any time.There are limited number of attempts which are specified by the user (currently non-available; 5). Game could be played solo or with friend in multi mode (currently under development; supposed to be added in v 2.0).

	# c) Used technology and methods
		The project was developed with the usage of Python 3.7.3 with the PyCharm IDE. Imported libs: random.

# 2. Setup

	Currently game operates on systems with Python 3.7.3. Suggested package Anaconda or Pycharm.

# 3. Algorithm step by step

	Hello and game mode pick(currently solo only).
	Word lists for each game mode (solo only, implemented list by the developers).
	Function: Generate random game_word for solo mode from the word_list_solo.
	Function: full_guess asks User to guess the game_word. If True User wins the game, else try again.
	Function: letter_guess asks User for a letter. If letter is in game_word informs and adds (later in main function) to guessed letters list. Same for wrong letter. Return both.
	Function: fill letters takes empty word, list of guessed letters and game word from main_function.
	Function chekcs if elements in the list of guessed letters are in game word; then fill empty word with these letters.
	Returns new empty word with filled letters.

	Function MAIN: Main launches and manages the program. First it generates random game word.
	Secondly, it creates empty word which will later show guessed letters in correct order.
	Function prints the word length as a tip. Also game has a limited number of attempts == 5.
	Creates two lists which are supposed to be updated with good/wrong letters (as a reminder and for fill_letters)
	In while function each time asks for the User decision, whether to make final guess or to pick a letter.
	If final guess then main goes to full_guess function. Upon return depends on if User wins or has to try again.
	After full_guess counter will subtract one attempt. Then return to the decision module split.
	If in decision User chose other then 'Yes' function uses letter guess module. As an effect it adds returns to lists.
	After module letter guess User loses one attempt. Then function informs about the result in the given info text.
	After informing User about list of letters program goes to fill letters which will replace "unknown mark" ('*') with letters from guessed letters list and will print the new word as a hint. If counter goes to zero User loses the game.

	Let's play the game! Using: main_function()

# 4. Known issues
	
	Currently multiplayer mode, expanded word list and number of attempts to be chosen by User are under development. Supposed to be added in v 2.0.
	While typing Yes/No in the beginning of the main_function program ignores capital letters. If typed anything then 'yes'/'Yes' function automatically uses option: 'No' and goes on.

# 5. Info about contributor.

	Development: Adrian Trzoss MA. PhD candidate at Faculty of History at Adam Mickiewicz University (AMU) in Poznan. Beginner in Python world. Great fun of oldschool rock music and tasty cooking.
