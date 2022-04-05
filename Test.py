"""LU Yes or No checking function
Simplifies the input by converting it to lower case. Also, accepts y or n as
abbreviations. Prints result of user choice as well as input - for testing.
"""


# Functions go here...
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


# Main routine goes here
show_instructions = yes_no("Have you played this game before?: ")
print(f"You entered '{show_instructions}")
print()
having_fun = yes_no("Are you having fun?: ")
print(f"You entered '{having_fun}")
