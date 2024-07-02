""" Instructions
💪 This is a difficult challenge! 💪

You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

    Take both people's names and check for the number of times the letters in the word TRUE occurs.

    Then check for the number of times the letters in the word LOVE occurs.

    Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is *z*." """

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

count_t = lowercase_name1.count('t') + lowercase_name2.count('t')
count_r = lowercase_name1.count('r') + lowercase_name2.count('r')
count_u = lowercase_name1.count('u') + lowercase_name2.count('u')
count_e1 = lowercase_name1.count('e') + lowercase_name2.count('e')
count_l = lowercase_name1.count('l') + lowercase_name2.count('l')
count_o = lowercase_name1.count('o') + lowercase_name2.count('o')
count_v = lowercase_name1.count('v') + lowercase_name2.count('v')
count_e2 = lowercase_name1.count('e') + lowercase_name2.count('e')

first_result = count_t + count_r + count_u + count_e1
second_result = count_l + count_o + count_v + count_e2

final_score = int(str(first_result) + str(second_result))

if (final_score < 10) or (final_score > 90):
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif (final_score >= 40) and (final_score <= 50):
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")
