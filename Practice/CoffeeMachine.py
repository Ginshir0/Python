options = [
    {
        "type": "epresso",
        "water": 50,
        "coffee": 18
    },
    {
        "type": "latte",
        "water": 200,
        "coffee": 24,
        "milk": 150
    },
    {
        "type": "cappuccino",
        "water": 250,
        "coffee": 24,
        "milk": 100
    },
]

# Starting Resources
water = 300
milk = 200
coffee = 100
money = 0

selection = input("What would you like? (espresso/latte/cappuccino): ")

if selection == "report":
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")

def getCash():
    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))