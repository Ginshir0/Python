print("Welcome to the tip calculator.")
totalBill =  int(input("What was the total bill? "))
peopleCount = int(input("How many people to split the bill? "))
tipPercentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

costPP = round(((totalBill / 100) * tipPercentage + totalBill) / peopleCount), 2

print(f"Each person should pay: {costPP}")