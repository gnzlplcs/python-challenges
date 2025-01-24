# easy version
# generate the passwrod in sequence. letters, then symbols, then numbers. if the user wants 4 letters 2 symbols and 3 numbers, then the password might look like this: fghj%$123
# you can see that all the letters are together. all the symbols are together and all the numbers follow each other as well. try to solve this problem first.

import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

""" easy_password = ""

for letter in range(0, nr_letters):
  easy_password += random.choice(letters)

for number in range(0, nr_numbers):
  easy_password += random.choice(numbers)

for symbol in range(0, nr_symbols):
  easy_password += random.choice(symbols)

print(easy_password) """

# hard password
selected_letters = []
selected_numbers = []
selected_symbols = []

for char in range(0, nr_letters):
  selected_letters += random.choice(letters)
for char in range(0, nr_numbers):
  selected_letters += random.choice(numbers)
for char in range(0, nr_symbols):
  selected_letters += random.choice(symbols)

combined_list = selected_letters + selected_numbers + selected_symbols
random.shuffle(combined_list)

hard_password = "".join(map(str, combined_list))

print(hard_password)
