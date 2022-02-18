def do_something():
    print("Ran function 'do_something'")


# Illustrate what you're trying to do
def query_user():
    user_input = input("""
Select A or B:
A: Do the thing now
B: Don't do the thing now
""")
    try:
        if user_input == "A":
            do_something()
        elif user_input == "B":
            #don't do anything.
            None
        else:
            raise(ValueError("You don't listen very well do you. I said Pick A or B..."))
        return
    except ValueError as e:
        print(e)
        print("This is how you handle specific errors")
        return



query_user()
query_user()
query_user()
query_user()
query_user()