print("Welcome to python pizza deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ") 

bill = 0

if size == "s" or size == "S":
    bill += 15
    if add_pepperoni == "y" or add_pepperoni == "Y":
        bill += 2
if size == "m" or size == "M":
    bill += 20
    if add_pepperoni == "y" or add_pepperoni == "Y":
        bill += 3
if size == "l" or size == "L":
    bill += 25
    if add_pepperoni == "y" or add_pepperoni == "Y":
        bill += 3
if extra_cheese == "y" or extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
