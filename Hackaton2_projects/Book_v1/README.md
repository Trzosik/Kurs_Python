# This is the Phone_book concept by Adrian Trzoss. Program manages the user's phone_book. Either creats or loads existing Phone_book.

# Contents:

1. Project Summary:
	a) Introduction
	b) Methods
	c) Used technology and methods
2. Setup
3. Algorithm step by step
4. Known issues
5. Info about contributor

# 1. Project Summary:

	# a) Introduction
		The Phone_book by Adrian Trzoss is a new program that manages the new or existing Phone_book implemented with Python programming language. Project was developed by the author as a part of his Python programming language course by Code:me in spring 2019. Current version: 1.0 Beta.

	# b) Methods
		Program starts with several functions: Load existing Phone_book; Starts new Phone_book; Saves changes to the existing or new file; Creats new record; Checks lenghts, Prints Phone_book; Finds records.

	# c) Used technology and methods
		The project was developed with the usage of Python 3.7.3 with the PyCharm IDE. Imported libs: json.

# 2. Setup

	Currently program operates on systems with Python 3.7.3. Suggested package Anaconda or Pycharm.

# 3. Algorithm step by step

	Program starts with an empty list that later will be mutable.
	Program shows menu window with options and asks user to give the number (pick function).
	Function: load_phone_book asks user to give file name that will be loaded.
	Function: start_new_book starts new Phone_book list.
	Function: Create_new_wpis creats new records consisting two keys: imie & numer; two values: nowe_imie & nowy numer. Ads to Phone_book. Excepts Value error in numer.
	Function: check_length informs user of the Phone_book records count.
	Function: print Phone_book returns all records (list of dicts) with keys and values.
	Function: Find_wpis gets from user key name and if in keys of given dict returns dict thats is being looked for.
	Function: Exit - ends the program.

	Function MAIN: Main operates on all functions as an infinite loop as long as user uses func: Exit that breaks the loop. If user gives wrong number or not int - function main gets back to the menu window.


# 4. Known issues
	
	Currently function find only returns wanted record (dict). Edition option is temporarly unavailable.

# 5. Info about contributor.

	Development: Adrian Trzoss MA. PhD candidate at Faculty of History at Adam Mickiewicz University (AMU) in Poznan. Beginner in Python world. Great fun of oldschool rock music and tasty cooking.
