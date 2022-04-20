"""Component 5 - statement formatter v1
"""


# welcome
text = "Welcome to the Lucky Unicorn Game"
sides = "-" * 3

formatted_text = f"{sides} {text} {sides}"
top_bottom = "-" * len(formatted_text)

print(top_bottom)
print(formatted_text)
print(top_bottom)
print()


# got unicorn
text = "Congratulations, you got a Unicorn!"
sides = "!" * 3

formatted_text = f"{sides} {text} {sides}"
top_bottom = "!" * len(formatted_text)

print(top_bottom)
print(formatted_text)
print(top_bottom)
print()


# end of game
text = "再见"
sides = "*" * 3

formatted_text = f"{sides} {text} {sides}"
top_bottom = "*" * len(formatted_text)

print(top_bottom)
print(formatted_text)
print(top_bottom)
print()
