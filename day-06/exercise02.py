sum_total = 0

while True:
	user_input = int(input("Enter a number (0 to quit): "))
	if user_input == 0:
		print(f"The total sum is {sum_total}")
		break
	sum_total+= user_input
