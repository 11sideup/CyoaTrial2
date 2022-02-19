#Define Multich as a multiple choice question:
def multich(ch1="Go North", ch2="Go South", ch3="Go East", ch4="Go West"):
    choice= input(f"""
    Select Option:
    A. {ch1}
    B. {ch2}
    C. {ch3}
    D. {ch4}""")
    return choice
    
Q1=multich()
print(f"You selected: {Q1}")
if Q1=='A':
    Q1a=multich(ch1="Die", ch2="Die", ch3="Die", ch4="Move On")
elif Q1=='B':
    Q1a=multich(ch1="Die", ch2="Die", ch3="Die", ch4="Move On")
elif Q1=='C':
    Q1a=multich(ch1="Die", ch2="Die", ch3="Die", ch4="Move On")
elif Q1=='D':
    Q1a=multich(ch1="Die", ch2="Die", ch3="Die", ch4="Move On")
else:
    raise(ValueError(f"Option {Q1} not supported"))
