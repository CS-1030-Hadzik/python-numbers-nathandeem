#TODO create a variable called my_int and store a two digit whole number in it
my_int = 52
print(my_int)

#TODO print out the following using my_int as the variable
#			binary value of my_int
#			octal value of my_int
#			hex value of my_int
print(bin(my_int))
print(oct(my_int))
print(hex(my_int))

#TODO create a variable with the current number of credits that you have earned in college.
# 			just count this class (4 credits) if you have not earned any credits
my_credits = 37
# create a second variable called AAS_credits required and assign it a value of 60 
AAS_credits = 60
# create a third variable called BS_credits required and assign it a value of 120
BS_credits = 120
# print out the following using the variables that you have just created.
# 			 'I have taken .... number of credits
# 			 'I have taken .... number of credits left until AAS degree (perform calculation)
# 			 'I have taken .... number of credits left until BS degree (perform calculation)
# 			 'I have .... percentage of AAS degree completed(perform calculation)
# 			 'I have .... percentage of BS degree completed(perform calculation)
# 			 'I have about .... number of classes left until AAS degree (perform calculation use 3 credit average class)
# 			 'I have about .... number of classes left until BS degree (perform calculation use 3 credit average class)
print(my_credits)
print(AAS_credits)
print(BS_credits)
print('I have taken', my_credits, 'credits')
print('I have', AAS_credits - my_credits, 'until AAS degree' )
print('I have', BS_credits - my_credits, 'until BS degree')
print('I have', (my_credits / AAS_credits)*100, 'percent of AAS degree completed')
print('I have', (my_credits / BS_credits)*100, 'percent of BS degree completed')
print('I have about', (AAS_credits - my_credits)//3, 'classes left until AAS degree')
print('I have about', (BS_credits - my_credits)//3, 'classes left until BS degree')

#TODO change the value of your my int variable to 64206
#			print converted my_int to binary
#			print converted my_int to octal
#			print converted my_int to hex
my_int = 64206
print(my_int)
print(bin(my_int))
print(oct(my_int))
print(hex(my_int))