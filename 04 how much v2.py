"""Component 2 (How much) v2
Use try/accept and pull error message out of the loop"""

error = "Please enter a whole number between 1 and 10\n"
valid = False

while not valid:
    try:
        money = int(input("How much would you like to play with? $"))
        if 0 < money <= 10:
            print(f"You're spending ${money} on the game.")
            valid = True
        else:
            print(error)

    except ValueError:
        print(error)
