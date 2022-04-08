"""Component 2 (How much) v4
Changing v2/3 into a function
Also needed to change money to the more generic variable name 'response'
and to change the condition and position of the number comparison into the loop
to make the function recyclable"""


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


# main routine
money = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with {money}")
