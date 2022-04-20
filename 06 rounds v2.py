"""Component 4 - game mechanics and looping v2
Based on 06 rounds v1
removed hard-wiring so that all tokens can be allocated (randint 1-100)
Gives user feedback about number of rounds and maintains balance
Test amount set to $5
"""

import random

# main routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT


rounds_played = 0
play_again = ""

# testing loop to generate 5 tokens
while play_again != "x":
    rounds_played += 1  # keep track of rounds
    number = random.randint(1, 100)

    # adjust balance
    # if the random number is between 1 and 5
    # user gets a unicorn (add $4 to balance)
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4

    # if the random number is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= number <= 36:
        token = "donkey"
        balance -= 1

    # in all other cases the token must be a horse or a zebra
    # (subtract $0.50 from the balance in either case)
    else:
        # if the number is even, set the token to zebra
        if number % 2 == 0:
            token = "zebra"
            balance -= .5
        else:
            token = "horse"
            balance -= .5

    # output
    print(f"Token: {token}, Balance: ${balance:.2f}")

print(f"Starting balance = ${TEST_AMOUNT:.2f}")
print(f"Final balance = ${balance:.2f}")
