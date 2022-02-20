# Import Person class
from Characters import NPC, PC

bob = PC(hp=10, attack=5, defense=5, magic=0, name="Bob", inventory="Butter Knife")
sally = NPC(hp=3, attack=1, defense=1, magic = 15, name="Sally", drops="Magic Wand")

# Do whatever if logic you want.

# Bob attacks sally for some reason
# Set Sally's health to 0
sally.hp = sally.hp-bob.attack
# Sally dies.
loot = sally.die()

# Bob collects magic wand
# You can do those in 1 line with bob.find_item(item=sally.die())
bob.find_item(item=loot)
# Print the console to show that bob's new item was added to his intentory list
print(bob.inventory)

# bob levels up and chooses to increase his attack stat
bob.attack = bob.attack+1

