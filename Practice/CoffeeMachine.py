options = [
    {
        "type": "epresso",
        "water": 50,
        "coffee": 18,
        "cost": 1.5
    },
    {
        "type": "latte",
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "cost": 2.5
    },
    {
        "type": "cappuccino",
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "cost": 3.0
    },
]

# Starting Resources
water = 300
milk = 200
coffee = 100
money = 0


def getReport():
    global water
    global milk
    global coffee
    global money

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

    totalCash = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return totalCash

def checkResources(h2o, dairy, caffeine):
    if h2o > water:
        print("“Sorry there is not enough water.")
        return False
    elif dairy > milk:
        print("“Sorry there is not enough milk.")
        return False
        
    elif caffeine > coffee:
        print("“Sorry there is not enough coffee")
        return False
    else:
        return True

power = True
while power:
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    # Turns off the machine and exits the program
    if selection == "off":
        power = False
    else:

    # provides a report of current resources available.
        if selection == "report":
            getReport()

        else:
            #convert selected drink into an index
            if selection == "espresso":
                drink = 0
            elif selection == "latte":
                drink = 1
            elif selection == "cappuccino":
                drink = 2
            #Check resources, funds provided, and process the order.
            if checkResources(options[drink]["water"], options[drink]["milk"], options[drink]["coffee"]):


                totalInserted = getCash()

                if totalInserted > options[drink]["cost"]:
                    money += totalInserted
                    print(f"Here is your {options[drink]["type"]} ☕ Enjoy")
                else:
                    print("“Sorry that's not enough money. Money refunded.")
