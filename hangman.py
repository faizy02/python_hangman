#!/usr/bin/env python3
# COPYRIGHT 2019 - HANGMAN - FAIZAN SAJJAD https://www.linkedin.com/in/faizan-sajjad-380a4b92/

import random

# GLOBAL VARIABLES
answer=[] 
allinput = []
turns = 0

def main():
	print("WELCOME TO THE HANGMAN GAME!!!")
	print("GUESS THE WORD. ONLY SINGLE LETTERS [A - Z] PER INPUT")
	win = False
	lose = False

	word = getword() # GETS THE WORD FROM THE FILE words.txt
	
	setupgame(word) # FILLS THE ANSWER ARRAY WITH '_'

	printanswer() # PRINTS THE USER ANSWER ARRAY 


	while(1):
		userinput = input("\nPLEASE ENTER YOUR LETTER:")
		
		allinput.append(userinput) # KEEP TRACK OF USER INPUTS
		
		updateArray(word,userinput,allinput) # UPDATE ARRAY IF USER INPUT IS CORRECT ELSE SUBTRACT THE TURNS
		
		printanswer()
		
		if '_' not in answer:
			win = True
			break

		if turns == 6:
			lose = True
			break

		#print("TURN REMAINING : {}".format(6-turns))
		printhangman()

	if win:
		print("YOU WIN !! YOU ARE AWESOME")
	if lose:
		printhangman()
		print("HANGED !!! BETTER LUCK NEXT TIME\n")
		
		print("YOUR INPUTS: ",end='')
		printinputs()

		print("\n\nTHE WORD WAS : " + word)


def getword():
	randomnumber = random.randrange(1,213)
	inputFile = open("words.txt", 'rt')
	counter = 0 
	
	for i in inputFile:
		if counter == randomnumber:
			word = i
			break
		counter += 1

	return word

def setupgame(word):
	length = len(word)
	i = 0
	while(i < length-1):
		answer.append('_')
		i += 1

def updateArray(word,userinput,allinput):
	
	global turns
	
	get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]

	if userinput in word: 
		indexes = get_indexes(userinput,word)
		for a in indexes:
			answer[a] = userinput.upper()

	else:
		turns += 1
		

def printanswer():
	print('\n')
	for i in answer:
		print(i + ' ',end='')
	print('\n')


def printinputs():
	for a in allinput:
		print(a+',',end='')

# PRINTS HANGMAN IN TEXT AND DISPLAYS REMAINING TURNS
def printhangman():
	global turns
	
	if turns == 0:
		print("""
   ____
  |    |      
  |        
  |        
  |    
  |   
 _|_
|   |______
|          |
|__________|
			""")
	elif turns == 1:
		print("""
   ____
  |    |      
  |    o      
  |       
  |   
  |   
 _|_
|   |______
|          |
|__________|
			""")
	elif turns == 2:
		print("""
   ____
  |    |      
  |    o      
  |    |   
  |    |
  |   
 _|_
|   |______
|          |
|__________|
			""")
	elif turns == 3:
		print("""
   ____
  |    |      
  |    o      
  |   /|    
  |    |
  |   
 _|_
|   |______
|          |
|__________|
			""")
	elif turns == 4:
		print("""
   ____
  |    |      
  |    o      
  |   /|\     
  |    |
  |   
 _|_
|   |______
|          |
|__________|
			""")
	elif turns == 5:
		print("""
   ____
  |    |      
  |    o      
  |   /|\    
  |    |
  |   /
 _|_
|   |______
|          |
|__________|
			""")
	elif turns == 6:
		print("""
   ____
  |    |      
  |    o      
  |   /|\    
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|
			""")
	print("TURNS REMAINING: {}".format(6-turns))


if __name__ == "__main__" : main()