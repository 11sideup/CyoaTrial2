# Import Person class
from Person import Person

#Equipped or Informed: A choose your own adventure.

# A method to call when there's bad input so I don't replicate error everywhere
def bad_input(input):
    raise(ValueError(f"Input value {input} not recognized."))

# Initialize the adventurer
Adventurer = Person()

# Start the adventure by selecting an initial option.
user_response=input("""You're in a dark cave. You should try to escape alive.
Choose option:
    A. Die
    B. Die Horrifically
    C. Look For Clues
    D. Look For Items
    """)
# Options and consequences of the first decision
if user_response =='A':
    Adventurer.print("You died.")
    Adventurer.die()
elif user_response =='B':
    Adventurer.print("You died horrifically.")
    Adventurer.die()
elif user_response =='C':
    consequence = input("""Choose option:
    A. Find Clue
    B. Die
    C. Die Badly
    """)
    if consequence =='A':
        Adventurer.print("You find a clue.")
        Adventurer.find_hint("TODO: Hint 1 message goes here.")
    elif consequence =='B':
        Adventurer.print("You died.")
        Adventurer.die()
    elif consequence =='C':
        Adventurer.print("You died. Badly...")
        Adventurer.die()
    else:
        bad_input(input=consequence)
elif user_response =='D':
    Adventurer.find_item(item="sword")
    consequence = input("""Choose option:
        A. Find Shield
        B. Die Helplessly
        """)
    if consequence == 'A':
        Adventurer.find_item("sheild")
    elif consequence =='B':
        Adventurer.print("You died helplessly.")
        Adventurer.die()
    else:
        bad_input(input=consequence)
else:
    bad_input(input=user_response)

# Merge the decision tree pathways if adventurer didn't die.
if not Adventurer.dead:
    user_response = input("""You made it to the hard part. Choose option:
    A. Go Left
    B. Go Right
    """)
    if user_response == 'A':
        Adventurer.find_item(item="armor")
        Adventurer.find_hint(hint="TODO: Put hint3 message here")
        consequence = input("""Choose option:
        A. Die Cold
        B. Die Hot
        C. Move On
        """)
        if consequence =='A':
            Adventurer.print("You freeze to death.")
            Adventurer.die()
        elif consequence =='B':
            print("You burn to death.")
            Adventurer.die()
        elif consequence =='C':
            another_consequence=input("""Choose option:
                A. Die Bald
                B. Move On
                """)
            if another_consequence =='A':
                Adventurer.print("You die bald.")
                Adventurer.die()
            elif another_consequence =='B':
               consequence_2 = input("""You move on.
                    Choose option:
                    A. Die Happy
                    B. Die Sad
                    C. Move On
                    D. Get Stuck?
                    """)
            else:
                bad_input(input = another_consequence)
        else:
            bad_input(input=consequence)