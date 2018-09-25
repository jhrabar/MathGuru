#John Hrabar
#SSW555
#I Pledge My Honor That I Have Abided By The Stevens Honor System

def power(number):
	return pow(2,number)


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


