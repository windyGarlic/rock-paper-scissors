'''
Rock Paper Scissors
~ Jordan Swebeck
15/02/23
ft:
⦁	include a welcome message to the game
⦁	read players’ names
⦁	account for all possibilities
⦁	accept input choices from both players
⦁	display output score (depending on choices)
⦁	display “Thank you for playing” message.
*	2 Player

'''
import getpass 


global Player1Name
global Player2Name
global Player1Score
global Player2Score
Player1Name = ""
Player2Name = ""
Player1Score = 0
Player2Score = 0 

def start(): 
	global Player1Name
	global Player2Name
	global Player1Score
	global Player2Score
	a = "Rock"
	b = "Paper"
	c = "Scissors"

#	Only run the firs bit of code once, so it doesnt keep asking for the player names.
#	It also gets the user input and hides the guess from the terminal.

	if Player1Name == "":
		input("Welcome to Rock Paper Scissors! Press any button to continue.")
		Player1Name = input("Can i get the first players name: ")
		Player2Name = input("Can i get the second players name: ")
		print(Player1Name)
		print("Ps. make sure you dont let the player see what number you pick if they look shifty.\n\n\n\n\n\n\n\n\n\n\n")
	print("Wins:\n" + Player1Name + ": " + str(Player1Score) + "\n" +Player2Name + ": " + str(Player2Score))
	print('Lets get started the choices are:\n1)Rock\n2)Paper\n3)Scissors')
	print("Note: If you want to stop the game type end, stop, or quit ")
	Player1Throw = getpass.getpass(prompt=Player1Name+"'s choice:")
	Player2Throw = getpass.getpass(prompt=Player2Name+"'s choice:")

#	Comparing all the possibities to see who wins.
	if Player1Throw or Player2Throw == 'end' or 'stop' or 'quit':
		print("Goodgame. Thanks for playing.")
		exit(0)
	if Player1Throw == "1" and Player2Throw == '2':
		print(Player2Name + " wins! Paper beats rock\n")
		Player2Score += 1
	elif Player1Throw == '1' and Player2Throw == "3":
		print(Player1Name + ' wins! Rock beats Scissors\n')
		Player1Score += 1
	elif Player1Throw == '1' and Player2Throw == "1":
		print("Its a tie, you both chose "+ a + "\n")

	elif Player1Throw == '2' and Player2Throw == "3":
		print(Player2Name + ' wins! Scissors beats paper\n')
		Player2Score += 1
	elif Player1Throw == '2' and Player2Throw == "1":
		print(Player1Name + " wins! Paper beats rock\n")
		Player1Score += 1
	elif Player1Throw == '2' and Player2Throw == "2":
		print("Its a tie, you bot chose " + b + '\n')

	elif Player1Throw == '3' and Player2Throw == "2":
		print(Player1Name + ' wins! Scissors beats paper\n')
		Player1Score += 1
	elif Player1Throw == '3' and Player2Throw == "1":
		print(Player2Name + " wins! Rock beats Scissors\n")
		Player2Score += 1
	elif Player1Throw == '3' and Player2Throw == "2":
		print("Its a tie, you bot chose " + c + "\n") 
	else:
		print("Something went wrong Sorry")
		start()
	
	start()

start()
