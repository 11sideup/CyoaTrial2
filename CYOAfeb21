###Standard Question Setup###
def multich(ch1="error1", ch2="error2", ch3="error3", ch4="error4"):
	choice= input(f"""
	Select Option:
		A. {ch1}
		B. {ch2}
		C. {ch3}
		D. {ch4}""")
	return choice
	
###Questions for naming and selecting play class.###
def givename():
	name= input(print("Type your name."))
	return name
def giveclass():
	playclass= multich(ch1='Warrior', ch2='Wizard', ch3='Cleric', ch4='Rogue')
	return playclass
	#add details about stats here
#name, position, items, attack, defense, health, magic, experience, level, playclass

###Define character class###
class Character:
	def __init__(self, name, position, items):
		self.name= name
		self.position= position
		self.items= items
#Setters and Getters for all Characters
#Name		
	def name(self):
		return self.name
	def name(self, value):
			self.value= value
#Position			
	def position(self):
		return self.position
	def position(self, value):
		self.value= value
#Items			
	def items(self):
		return self.items
	def items(self, value):
		self.value= value
###//Define NPC Subclass//###
###Not needed since they only need character parameters###

###Start NPC Bob###
bob= Character('Bob', 'Town', 'Main Key')
#Function for printing bob.
def bobsheet():
	print(f"""
	Name: {bob.name}
	Position: {bob.position}
	Items: {bob.items}""")
#Printing Bob
#bobsheet()	
	
###Define Battlers###
class Battler(Character):
	def __init__(self, name, position, items, attack, defense, health, magic, experience, level, playclass):
		self.name= name
		self.position= position
		self.items= items
		self.attack= attack
		self.defense= defense
		self.health= health
		self.magic= magic
		self.experience= experience
		self.level= level
		self.playclass= playclass
#name, position, items, attack, defense, health, magic, experience, level, playclass
###        ###          ###          ###         ###
###Setters and Getters for Battlers###
#Attack	
	def attack(self):
		return self.attack
	def attack(self, value):
		self.value= value
#Defense	
	def defense(self):
		return self.defense
	def defense(self, value):
		self.value= value
#Health
	def health(self):
		return self.health
	def health(self, value):
		self.value= value	
#Magic
	def magic(self):
		return self.magic
	def magic(self, value):
		self.value= value	
#Experience	
	def experience(self):
		return self.experience
	def experience(self, value):
		self.value= value
#Level
	def level(self):
		return level.health
	def level(self, value):
		self.value= value	
#Playclass
	def playclass(self):
		return self.playclass
	def playclass(self, value):
		self.value= value
		
###Start PC 'player'.###
player= Battler(givename(), "Town", None, 1, 1, 1, 'none', 0, 1, giveclass())
if player.playclass== 'A':
	player.playclass='Warrior'
	player.items= 'Sword'
	player.attack= 5
	player.defense= 10
	player.health= 15
	player.magic= 'None'
elif player.playclass=='B':
	player.playclass='Wizard'
	player.items='Wand'
	player.attack= 10
	player.defense= 5
	player.health= 10
	player.magic= 'Fire'
elif player.playclass=='C':
	player.playclass='Cleric'
	player.items='Relic'
	player.attack= 4
	player.defense= 10
	player.health= 12
	player.magic= 'Heal'
elif player.playclass=='D':
	player.playclass='Rogue'
	player.items='Dagger' +' ' + 'Lockpick'
	player.attack= 8
	player.defense= 8
	player.health= 10
	player.magic= 'None'
else:
		None

#Function to level up player#
def levelup():
		check=player.level
		if player.experience<5:
			player.level= 1
		elif player.experience<10:
			player.level= 2
		elif player.experience<20:
			player.level= 3
		elif player.experience>20:
			player.level= 4
		else:
			None
		if player.level != check:
			print("You leveled up!")
		else:
			None
		
#Function to call player statblock
def playerstatblock():
	self= player
	statblock=print(f"""
	Name: {self.name}
	Position: {self.position}
	Items: {self.items}
	Attack: {self.attack}
	Defense: {self.defense}
	Health: {self.health}
	Magic: {self.magic}
	Experience: {self.experience}
	Level: {self.level}
	Class: {self.playclass}""")
	return self
playerstatblock()

###Enemies given classes that will later be associated with different outcomes based on what stats the player has.###

###Initiate Battler minotaur###
minotaur= Battler('Minotaur', "Dungeon", 'Health Potion', 12, 6, 20, 'None', 5, 1, 'Beast')
def minotaurstatblock():
	self= minotaur
	statblock=print(f"""
	Name: {self.name}
	Position: {self.position}
	Items: {self.items}
	Attack: {self.attack}
	Defense: {self.defense}
	Health: {self.health}
	Magic: {self.magic}
	Experience: {self.experience}
	Level: {self.level}
	Class: {self.playclass}""")
#minotaurstatblock()

###Function for performing a battle with the minotaur.###
def minotaurbattle():
	print("A minotaur blocks your path. You must fight or flee")
	choice=multich(ch1='Fight', ch2='Flee')
	if choice=='A':
		print("You decide to fight.")
		player.items= player.items + ' ' + minotaur.items
		minotaur.items= None
		player.experience= player.experience + minotaur.experience
		minotaur.health= minotaur.health - (player.attack - minotaur.defense)
		if player.playclass== 'Wizard':
			print(f"Your {player.magic} magic defeats the minotaur. You gain {minotaur.experience} experience.")
		elif player.playclass!='Wizard':
			print(f"You fight the minotaur and take {minotaur.attack - player.defense} damage.")
			player.health= player.health - (minotaur.attack - player.defense)		
#Define choice B		
	elif choice=='B':
		print("You decided to flee.")
	else:
		None
	return choice

def mino_encounter():
	minotaurbattle()
	levelup()
	playerstatblock()
	return None

mino_encounter()
minotaurstatblock()
