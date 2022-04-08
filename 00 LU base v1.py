"""Lucky Unicorn base component
Components added after they have been created and tested"""


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


# number checking function
def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    while True:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here
played_before = yes_no("Have you played this game before?: ").lower()

if played_before == "no":
    instructions()


# ask the user how much they want to play with
money = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with {money}")
