#Program to simulate Rock paper scissor in Python

from random import randint

#Creating list of the actions to be done
m = ["Rock", "Paper", "Scissors"]

#Asssigning a random variable for computer to play
computer = m[randint(0,2)]

#Setting player to False
player = False

while player == False:
	#setting player to true
	player = input("Rock, Paper, Scissors?")
	if player == computer:
		print("Tie!!")
	elif player == "Rock":
		if computer == "Paper":
			print("Computer wins")
		else:
			print("Player wins")
	elif player == "Paper":
		if computer == "Scissors":
			print("Computer wins")
		else:
			print("Player wins")
	elif player == "Scissors":
		if computer == "Rock":
			print("Computer Wins")
		else:
			print("Player wins")
	else:
		print("Invalid input. Please check thoroughly!!!")

#setting the player as false in order to let the loop continuw
player = False
computer = m[randint(0,2)]