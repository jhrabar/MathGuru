#John Hrabar, Matt Swentzel, Jaroor Modi
#SSW555
#I Pledge My Honor That I Have Abided By The Stevens Honor System

def power(number):
	#returns the number to the power of 2
	return pow(2,number)

def factorial(number):
	#returns the factorial of a given number
	if(number == 0):
		return 1
	return number * factorial(number - 1)

def fab(number):
	#returns the nth fibonacci number, starting with index 1
	if number <= 0:
		print('ERROR: Input must be greater than 0')
		return -1
	elif number == 1:
		return 0
	elif number == 2:
		return 1
	else:
		return fab(number-1)+fab(number-2)
		

while(True):
	while(True):
		method = input("Please input \n\tpow to calculate the nth power of 2\n\tfactorial to calculate n factorial\n\tfab to calculate the nth number of the fibonacci sequence\n")
		if(method == "pow" or method == "factorial" or method == "fab"):
			break
	while(True):
		n = int(input("Please input a number\n"))
		if(n > 20 or n < 0):
			print("Number entered must be between 0 and 20")
		else:
			break
	if(method == "pow"):
		result = power(n)
		print("The result is: " + str(result))
	elif(method == "factorial"):
		result = factorial(n)
		print("The result is: " + str(result))
	else:
		result = fab(n)
		print("The result is: " + str(result))
	while(True):
		cont = input("Would you like to continue? Enter yes or no\n")
		if(cont == "yes" or cont == "no"):
			break
	if(cont == "no"):
		print("Goodbye!")
		break
