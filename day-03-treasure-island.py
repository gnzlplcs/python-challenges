print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇
first_question = input("You're at a crosroad. Where do you want to go? Type 'left' or 'right' ")

if first_question == "left":
  second_question = input("You've come to a lake. There is an island in the middle of the lake. Do you want to wait for a boat or swim? Type 'wait' or 'swim' ")
  print(second_question)
  if second_question == 'wait':
    third_question = input("Awesome! You're almost a winner. Just one last question: Which door do you choose to continue? Please, type 'red', 'yellow', or 'blue' ")
    print(third_question)
    if third_question == 'red':
      print("Burned by fire. Game Over.")
    elif third_question == 'yellow':
      print("You win!")
    elif third_question == 'blue':
      print("Eaten by beasts. Game Over")
    else:
      print("Game Over.")
  else:
    print('Attacked by trout. Game Over.')
else:
  print("You fell into a hole. Game Over.")