print("Program begin")

while True:
	print("Options:")
	print("Enter 'add' or '+' to add numbers")
	print("Enter 'subtract' or '-' to subtract numbers")
	print("Enter 'multiply' or '*' to multiply numbers")
	print("Enter 'divide' or '/' to divide numbers")
	print("Enter 'quit' to end the program")
	user_input = input("Enter: ")
	if user_input == "quit":
		break
	elif user_input == "+" or user_input == "add":
		cou = 0
		res = 0
		a = float(input("Enter count of number: ")) - 1
		num = []
		while a >= cou:
			num.append(float(input("Enter a number: ")))
			cou += 1
		print(sum(num)) #auto-summ of massive
	elif user_input == "-" or user_input == "substract":
		cou = 0
		a = float(input("Enter count of number: ")) - 1
		num = []
		while a >= cou:
			num.append(float(input("Enter a number: ")))
			cou += 1
		res = num[0]
		cou = 1
		while a >= cou:
			res = res - num[cou]
			cou += 1
	elif user_input == "*" or user_input == "multiply":
		cou = 0
		res = 0
		a = float(input("Enter count of number: ")) - 1
		num = []
		while a >= cou:
			num.append(float(input("Enter a number: ")))
			cou += 1
		res = num[0]
		cou = 1
		while a >= cou:
			res = res * num[cou]
			cou += 1
	elif user_input == "/" or user_input == "divide":
		cou = 0
		res = 0
		a = float(input("Enter count of number: ")) - 1
		num = []
		while a >= cou:
			num.append(float(input("Enter a number: ")))
			cou += 1
		res = num[0]
		cou = 1
		while a >= cou:
			res = res / num[cou]
			cou += 1
	else:
		print("Unknown input")
	if user_input == "+" or user_input == "add":
		None
	else:
		print(res)
print("Program ended")