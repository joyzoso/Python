#python tictactoe game
version 2!!!
import random
import sys

board = range(0,9)

def show():
	print board[0], '|', board[1], '|', board[2]
	print '--------'
	print board[3], '|', board[4], '|', board[5]
	print '--------'
	print board[6], '|', board[7], '|', board[8]


show()

def checkLine(char, spot1, spot2, spot3):
	if board[spot1] == char and board[spot2] == char and board[spot3] == char:
		return True

def checkAll(char):
	if checkLine(char, 0, 1, 2):
		return True
	if checkLine(char, 3, 4, 5):
		return True
	if checkLine(char, 6, 7, 8):
		return True
	if checkLine(char, 0, 3, 6):
		return True
	if checkLine(char, 1, 4, 7):
		return True
	if checkLine(char, 2, 5, 8):
		return True
	if checkLine(char, 0, 4, 8):
		return True
	if checkLine(char, 6, 4, 2):
		return True



while True:

	input = raw_input("Choose a spot") #this statement causes the loop to stop
	input = int(input)

	if board[input] != 'x' and board[input] != 'o':
		board[input] = 'x'
		show()

		if checkAll('x') == True: #check for X
			print "**X IS THE WINNER!"
			print show()
			sys.exit()
			break;

	while True: #computer looking for an available spot

		random.seed() #provides random generator
		opponent = random.randint(0,8)
		if board[opponent] != 'o' and board[opponent] !='x':
			board[opponent]= 'o'
			if checkAll('o') == True: #check for O
				print "**O IS THE WINNER!"
				show()
				sys.exit()
				break;

			break;

	else:
		print "That spot is taken"


show()
