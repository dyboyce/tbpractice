for num in range (1,100):
	string = ""
	if num % 3 == 0 and num % 5 == 0:
		print('FizzBuzz')
	elif num % 5 == 0:
		print('Buzz')
	if num % 5 != 0  and num % 3 != 0:
		string = string + str(num)
	print(string)
 
