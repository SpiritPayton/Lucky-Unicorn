"""LU Yes or No
Simplifies the input by converting it to lower case. Also, accepts y or n as
abbreviations. Prints result of user choice as well as input - for testing.
"""

show_instructions = ""
while show_instructions != "x":

    # Ask user if they have played the game before
    show_instructions = input("Have you played this game before?: ").lower()

    # If they say yes, output "Program Continues"
    if show_instructions == "yes" or show_instructions == "y":
        print("Program continues")

    # If they say no, output "Display Instructions"
    elif show_instructions == "no" or show_instructions == "n":
        print("Display instructions")

    # Otherwise, show error
    else:
        print("Please enter 'yes' or 'no'.")

    print(f"You entered '{show_instructions}'.")
