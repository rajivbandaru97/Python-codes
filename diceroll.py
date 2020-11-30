#Program to print a rolling dice using Python
import sys
import random

minval = int(input('Enter the minimum value of the dice: '))
#Writing a condition to keep the miinimum value equal to 1
if minval == 1:
	print(minval)
else:
	print('Invalid input')
	exit() #This function is used in order to terminate the program
maxval = int(input('Enter the maximum value of the dice: '))
#Writing a condition to keeep in check the maximum value is not greater than 6
if maxval <= 6:
	print(maxval)
else:
	print('Invalid input')
	exit()
again = True
while again:
	print(random.randint(minval, maxval))

	more_roll = input('Wish to roll the dice again?')
	if more_roll == 'yes' or more_roll == 'y':
		again = True
	else:
		again = False