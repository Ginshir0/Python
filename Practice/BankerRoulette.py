import random

names_string = input("Please provide a list of names separated by a comma followed by a space:\n")
names = names_string.split(", ")

chosen = random.randint(0, len(names) - 1)

print(f"{names[chosen]} is going to buy the meal today!")
