import random

rock = '''
    ______
---'  ____)_
     (______)
     (______)
      (____)
---.__(___)
'''

paper = '''
    ______
---'   ___)____
          ______)
       __________)
      __________)
---.__________)
'''

scissors = '''
    ______
---'   ___)_____
          ______)
      __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]
names = ['piedra', 'papel', 'tijeras']

user_choice = int(input('¿Qué escoges? \nIngresa 0 para piedra, \n1 para papel \n2 para tijeras.'))
computer_choice = random.randint(0, 2)

result = ''

if user_choice == computer_choice:
  result = 'Empataste'
elif user_choice == 0:
  if computer_choice == 1:
    result = 'Perdiste'
  elif computer_choice == 2:
    result = 'Ganaste'
elif user_choice == 1:
  if computer_choice == 0:
    result = 'Ganaste'
  elif computer_choice == 2:
    result = 'Perdiste'
elif user_choice == 2:
  if computer_choice == 0:
    result = 'Perdiste'
  elif computer_choice == 1:
    result = 'Ganaste'
else:
  result = 'Selección inválida'

print(f'''
  Escogiste {names[user_choice]}
  {options[user_choice]}
''')

print(f'''
  La computadora escogió {names[computer_choice]}
  {options[computer_choice]}
''')

print(result)
