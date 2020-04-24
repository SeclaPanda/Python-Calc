print("Program begin")
"""
a = input('Enter number 1:') User input
b = input('Enter number 2:')
if a > b: 
	print(a) 
	print(b)
elif a == b: if if if - bullshit if elif elif - good code
 	print("Number is equal")
else:
	print(b)
	print(a)
print('spam'*3) you can multiply word
a = 20
b = a / 6 
c = a % 6
print(a, b, c)
"""
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