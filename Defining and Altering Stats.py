###MAJOR QUESTIONS###
### Can I get the code to display the number of options given and not others?###

###Standard Question Setup###
def multich(ch1="error1", ch2="error2", ch3="error3", ch4="error4"):
	choice= input(f"""
	Select Option:
		A. {ch1}
		B. {ch2}
		C. {ch3}
		D. {ch4}""")
	return choice
###Because of how this is set up you need to define ch1-ch4 as the question options when you call the function.###

###Give a specific multiple choice question for choosing playclass.###
def playclass():
	playclass= multich(ch1='Fighter', ch2='Wizard', ch3='Cleric', ch4='Rogue')
	return playclass

###Define Character###
class Person:
	def __init__(self, hp, attack, defense, magic, name, alive, playclass, inventory):
		self.hp=hp
		self.attack=attack
		self.defense=defense
		self.magic=magic
		self.name=name
		self.alive=alive
		self.playclass=playclass
		self.inventory=inventory
		
###make them give a name###		
def givename():
	    name=input(print('type your name'))
	    return name

###Start Player###
bob= Person(1, 1, 1, 'none', givename(), True, playclass(),'empty')
	
###Alter stats based on playclass selection###
if bob.playclass=='A':
	bob.hp=10
	bob.attack=5
	bob.defense=5
	bob.magic='None'
	bob.playclass='Fighter'
	bob.inventory='Sword'
elif bob.playclass=='B':
	bob.hp=5
	bob.attack=10
	bob.defense=5
	bob.magic='Fire'
	bob.playclass='Wizard'
	bob.inventory='Wand'
elif bob.playclass=='C':
	bob.hp=8
	bob.attack=4
	bob.defense=8
	bob.magic='Heal'
	bob.playclass='Cleric'
	bob.inventory='Holy Symbol'
elif bob.playclass=='D':
	bob.hp=5
	bob.attack=8
	bob.defense=8
	bob.magic='None'
	bob.playclass='Rogue'
	bob.inventory='Dagger' + ' and ' + 'Lockpick'
else:
	raise(ValueError(f"Option {bob.playclass} not supported."))
	
###Determine if player is alive. this function calls when statblock() is called###
def alive():
	if bob.hp>0:
		bob.alive=True
	else:
		bob.alive=False
		if bob.alive==False:
			print("You have died.")
	return bob.alive

###function to print your statblock and recheck living status###
def statblock():
	alive()
	print(f"""
Your hp is {bob.hp}.
Your attack is {bob.attack}.
Your defense is {bob.defense}.
Your magic is {bob.magic}.
Your name is {bob.name}.
Your living status is {bob.alive}.
Your class is {bob.playclass}.
Your inventory is {bob.inventory}.
""")

statblock()

###Function for giving health potion
def healthpot():
	bob.inventory=bob.inventory + ' and ' 'Health Potion'
	
###Function for fighting minotaur. Wizards win. Rogues lose.
def minotaur():
			if bob.playclass != 'Wizard':
				bob.hp=bob.hp-6
				healthpot()
				print("You take a blow during the fight!")
			elif bob.playclass == 'Wizard':
				healthpot()
				print("Your fire magic deftly defeats the minotaur!")
			else:
				None
								
#Function for fleeing from battle. Rogues dont lose hp.
def flee():
			if bob.playclass!='Rogue':
				print('You run and lose 2 HP from tripping over a rock.')
				bob.hp=bob.hp-2
			else:
				print("You deftly escape.")
				
###Function that integrates the fight/flee functions for the minotaur battle. on Q1a
def minofight():
	if Q1a=='A':
		minotaur()
	elif Q1a=='B':
		flee()
	else:
		None
	
###Question 1###

#Call Q1.
Q1=multich(ch1='Go North', ch2='Go South', ch3='Go West', ch4='Go East')
#Define options Q1a
if Q1=='A':
	print("Enemy appears! You must face this foe head on in combat or flee for your life! A menacing looking minotaur blocks your path!")
	Q1a=multich(ch1='Fight', ch2='Flee')
	minofight()
#Q1a Terminates
#
else:
	None


statblock()
#Q1a terminates and you are either alive or dead. Your stats display.

				
"""

elif Q1=='B':
	print('The end.')
elif Q1=='C':
	print('The other end.')
elif Q1=='D':
	print('The last end.')
else:
	raise(ValueError(f"Option {Q1} not supported."))
	
"""
