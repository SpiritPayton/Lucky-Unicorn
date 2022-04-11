"""Component 3 (random tokens) v3
Calculate user balance based on random selection of tokens """

import random

tokens = ["unicorn",
          "horse", "donkey", "zebra",
          "horse", "donkey", "zebra",
          "horse", "donkey", "zebra"]
STARTING_BALANCE = 100
balance = STARTING_BALANCE

for item in range(500):
    token = random.choice(tokens)
    print(token, end='\t')

    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= .50

print(f"Starting balance = ${STARTING_BALANCE:.2f}")
print(f"Final balance = ${balance:.2f}")
