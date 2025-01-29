password = "python"
attempts = 0

while attempts < 3:
	user_input = str(input("Enter the password: "))
	if user_input == "python":
		print("Access granted!")
		break
	else:
		print("Try again")
		attempts += 1
else:
	print("No more attempts")