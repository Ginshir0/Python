import random

options = ["Rock", "Paper", "Scissor"]
cpu = random.randint(0, 2)

print("Welcome to a game of Rock, Paper, Scissor.")
player = int(input("Please enter [0] for Rock, [1] for Paper, or [2] for Scissor"))
print(options[cpu])

if options[player] == options[cpu]:
    print(f"You chose {options[player]} and the CPU chose {options[cpu]} ")
