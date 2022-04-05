"""Took function from other component as the basis for this new function which
incorporates both yes/no and show instructions"""


# yes/no checking function...
def yes_no(question_text):
    while True:

        # Ask user if they have played the game before
        answer = input("Have you played this game before?: ").lower()

        # If they say yes, output "Program Continues"
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output "Display Instructions"
        elif answer == "no" or answer == "n":
            answer = "no"
            return answer

        # Otherwise, show error
        else:
            print("Please enter 'yes' or 'no'.")


# Function to display instructions
def instructions():
    print("**** How to play ****")
    print()
    print("The rules of the game will go here")
    print()
    print("Program continues")
    print()


# Main routine goes here
played_before = yes_no("Have you played this game before?: ").lower()

if played_before == "no":
    instructions()
else:
    print("Program continues")
