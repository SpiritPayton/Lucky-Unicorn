"""Component 2 (How much) v1
Ask user how much they want to play with and check that the input is a valid
integer between 1 and 10. If it is, this amount becomes the balance in their
account"""


money = int(input("How much money do you want to spend on playing? (between $1 and $10) $"))

while not 1 <= money <= 10:
    print("Only whole numbers between $1 and $10 please")
    money = int(input("How money do you want to spend on playing? $"))

print(f"You're spending ${money} on the game")
