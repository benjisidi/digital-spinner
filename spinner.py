import random
import sys

#Player Class
class player:
	def __init__(self, name):
		self.name = name
		self.lHand = "unassigned"
		self.lFoot = "unassigned"
		self.rHand = "unassigned"
		self.rFoot = "unassigned"
		self.turn = 0
		self.startOrder = random.sample(range(0,4), 4) #This is the order in which their limbs will be allocated a colour over turns 1-4

	#Function for debugging: prints the status of a player
	def sitrep(self):
		print "\n---SITREP---\nName: ", self.name, "\n Left Hand: ", self.lHand, "\n Left Foot: ", self.lFoot,\
		"\nRight Hand: ", self.rHand, "\nRight Foot: ", self.rFoot, "\nTurn: ", self.turn, "\nStart Order: ", self.startOrder, "\n"

	#Twist function issues an instruction to the player
	def twist(self):
		limbs = ["left hand",  "left foot", "right hand", "right foot"]
		limbrefs = ["lHand", "lFoot", "rHand", "rFoot"]
		colours = ["red", "blue", "green", "yellow"]
		limb_number = random.randint(0,3)
		colour_number = random.randint(0,3)
		turn = self.turn
		#During the first 4 turns, follow a player's startOrder to allocate all their limbs a colour
		if turn < 4:
			setattr(self, limbrefs[self.startOrder[turn]], colours[colour_number])
			print self.name.upper() + ": " + limbs[self.startOrder[turn]] + " " + colours[colour_number]			
		else:
			#Ensure players do not get allocated a limb/colour combination they're already on
			while getattr(self, limbrefs[limb_number]) == colours[colour_number]: colour_number = random.randint(0,3)
			setattr(self, limbrefs[limb_number], colours[colour_number])
			print self.name.upper() + ": " + limbs[limb_number] + " " + colours[colour_number]
		setattr(self, "turn", turn + 1)


def run_game():
	#---Setup Phase---
	#Input number of players
	while True: 
		try: 
			numPlayers = int(raw_input("Enter number of players (2-16): "))
			while numPlayers < 2 or numPlayers > 16: 
				numPlayers = int(raw_input("You might have difficulty playing with that number of people. Please choose between 2 and 16: "))
			break
		except ValueError: 
			print "That wasn't a integer!"
	#Fill array with players and assign them names
	players = []
	for i in range(0, numPlayers):
		playername = raw_input("Name of player " + str(i + 1) + ": ")
		while playername == "":
			playername = raw_input("Playernames cannot be blank.\nPlease name player " + str(i + 1) + ": ")
		players.append(player(playername))

	#---Game Phase---
	print "Press ENTER to spin, or type 'eliminate' to remove a player and 'exit' to end the game."
	counter = 0 #This is the turn counter used to keep track of whose go it is
	while True:
		command = raw_input()
		while command not in ['exit', 'eliminate', '']:
			command = raw_input("\nSorry, '" + command + "' is not a valid command.\nType 'eliminate' to eliminate a player, 'exit' to exit or press ENTER to spin.\n")
		if command.lower().strip() == 'exit': sys.exit(0)
		#Procedure for eliminating a player
		if command.lower().strip() == 'eliminate':
			#List players and their corresponding numbers
			for i in range(0, len(players)):
				print str(i+1) + ": " + getattr(players[i], "name").upper()
			#Ask which player is to be eliminated
			while True:
				try:
					eliminated = int(raw_input('Enter player number to be eliminated: '))
				 	while eliminated not in range(1, len(players)+1):
				 		eliminated = int(raw_input("That's not a valid player number. Try again: "))
				 	print getattr(players[eliminated-1], "name").upper() + " eliminated!\n"
				 	#Adjust counter to preserve player order; don't do this if nobody has played yet,
				 	#or if the last player has just gone.
				 	if counter > 0 and counter%len(players)!=len(players): counter -= 1
				 	#Remove the eliminated player from the array
				 	players.pop(int(eliminated)-1)
				 	break
				except ValueError:
				 	print "That's not an integer!"
			#Automatically end the game when only one player remains.
			if len(players) == 1:
				print "---" + getattr(players[0], "name").upper() + " wins!---\n\n"
				break
		#If no command is given, give current player an instruction and increment the counter
		else:
			players[counter%len(players)].twist()
			counter += 1		

def main():
	print "\n---Welcome to digital spinner!---\n"
	while True:
		run_game()
		command = raw_input('---Game over!---\nType "exit" to exit or "new" for new game.')
		while command.lower().strip() not in ['exit', 'new']:
			command = raw_input('Sorry, "' + command + '" is not a valid command.\nType "exit" to exit or "new" for new game.\n')
		if command.lower().strip() == 'exit': sys.exit(0)

if __name__ == '__main__':
	main()