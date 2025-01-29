""" Exercise 1: Number Guessing Game
Write a program that generates a random number between 1 and 100 and asks the user to guess it. The program should:
1. Tell the user if their guess is too high or too low.
2. Keep track of the number of guesses.
3. End the game when the user guesses the correct number.
Hints:
+ Use the random module to generate a random number.
+ Use a while loop to keep asking for guesses until the user gets it right.
+ Use if statements to check if the guess is too high or too low."""

import random


def ask_number():
	while True:
		try:
			return int(input("Guess the number (between 1 and 100): "))
		except ValueError:
			print("Invalid input. Please enter a number.")


def guessing_game():
	secret_number = random.randint(1, 100)
	attempts = 0

	while True:
		user_number = ask_number()
		attempts += 1

		if user_number < secret_number:
			print("Too low!")
		elif user_number > secret_number:
			print("Too high!")
		else:
			print(f"You win! The secret number is {secret_number}.")
			print(f"It took you {attempts} attempts.")
			break


# Run the game
guessing_game()
