line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

column = str(position[0].lower())
row = str(position[1].lower())

if column == 'a':
  column = 0
elif column == 'b':
  column = 1
elif column == 'c':
  column = 2
else:
  input('Wrong coordinate entered')

if row == '1':
  row = 0
elif row == '2':
  row = 1
elif row == '3':
  row = 2
else:
  input('Wrong coordinate entered')

map[row][column] = 'X' # type: ignore

# print(column,row)

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
