""" Instructions

You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

NOTE: In this exercise, you are working collaboratively with another programmer. They already dealt with input() and writing the code needed to get hold of the names in the input area, so you don't need to worry about that.

The other programmer has written the code to separate the names in the input area into individual names and puts them inside a List called names. For their code to work correctly, you must enter all the names in the input area followed by comma then space. e.g. name, name, name

You can try printing names to see what it looks like (but remember to remove that code when you submit the assignment). """

import random

names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

num_names = len(names)
random_num = random.randint(0, num_names - 1)
payer = names[random_num]

# payer = random.sample(names, 1)

result = f"{payer} is going to buy the meal today!"
# result = f"{payer[0]} is going to buy the meal today!"

print(result)
