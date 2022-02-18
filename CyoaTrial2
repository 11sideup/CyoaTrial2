#This one works right now. It currently does not perform goback like I think it should I don't know how to make it do so. 

#Define Parameters
Q1c=0
Q1cd=0

hint1=0
hint2=0
hint3=0
hint4=0

sword=0
shield=0
armor=0
wand=0

Q1=0
Q2=0
Q3=0

goback=0

print("Start")
Q1=input(print("""Choose Option:
A. Die
B. Die Horribly
C. Explore"""))
if Q1=='A':
    print("You die.")
if Q1=='B':
    print("You die horribly.")
if Q1=='C':
    Q1c=input(print("""You explore. Choose Option:
    A. Hunt Item
    B. Die Hot
    C. Die Cold
    D. Search For Clue"""))
    if Q1c=='A':
        sword=1
        print("You find a sword!")
    if Q1c=='B':
        print("You burn to death.")
    if Q1c=='C':
        print("You freeze to death.")
    if Q1c=='D':
        hint1=1
        print("You find hint1!")
        Q1cd=input(print("""Choose Option:
        A. Search For Hint
        B. Die Peacefully"""))
        if Q1cd=='A':
            hint2=1
            print("You find hint2!")
        if Q1cd=='B':
            print("You die peacefully.")
if Q1c=='A' or Q1cd=='A':
    print("Now for the hard part.")
    Q2=input(print("""Select Option:
    A. Go Left
    B. Go Right"""))
    if Q2=='A':
        print("You find hint3! You find a shield!")
        hint3=1
        shield=1
        Q2a=input("""Choose Option:
        A. Die Old
        B. Die Young
        C. Move On""")
        if Q2a=='A':
            print("You die old.")
        if Q2a=='B':
            print("You die young.")
        if Q2a=='C':
            print("You move on.")
            Q2ac=input(print("""Choose Option:
            A. Die Now
            B. Move On"""))
            if Q2ac=='A':
                print("You die now.")
            if Q2ac=='B' or goback==1:
                print("You move on.")
                Q2acb=input(print("""Choose Option:
                A. Die Happy
                B. Die Sad
                C. Move On
                D. Get Lost"""))
                if Q2acb=='A':
                    print("You die happy.")
                if Q2acb=='B':
                    print("You die sad.")
                if Q2acb=='C':
                    print("You move on.")
                if Q2acb=='D':
                    print("You get lost.")
                    Q2acbd=input("""Choose Option:
                    A. Die
                    B. Die
                    C. Go Back""")
                    if Q2acbd=='A':
                        print("You die.")
                    if Q2acbd=='B':
                        print("You die.")
                        if Q2acbd=='C':
                            goback=1
                        
