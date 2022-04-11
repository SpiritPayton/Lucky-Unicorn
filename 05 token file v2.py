"""Component 3 (random tokens) v2
Calculate user balance based on random selection of tokens """

import random

tokens = ["unicorn", "horse", "donkey", "zebra"]
balance = 100

for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')

    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= .50

    print(f"Token: {token}, Balance: ${balance}")
