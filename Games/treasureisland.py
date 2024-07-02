print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
answer = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"").lower()

if answer == "left":
    print("You choose to go left and after a few miles you come across a lake")
    answer = input("Would you like to \"swim\" or \"wait\"").lower()
    if answer == "wait":
        print("As you wait an empty boat approaches and you got on to get across")
        answer = input("You finally reach the end but there is 3 doors. "
                       "Which door do you choose? yellow, red, or blue").lower()

        if answer == "yellow":
            print("You found the treasure behind the yellow door.\n YOU WIN!")
        elif answer == "red":
            print("Opening the red door activated a trap of fire. your burned to ashes.\nGAME OVER.")
        elif answer == "blue":
            print("Behind the blue door you find yourself surrounded by beasts and eaten.\nGAME OVER.")
        else:
            print("GAME OVER.")
    else:
        print("Not long after you started swimming you get eaten by piranhas.\nGAME OVER.")

else:
    print("While walking you activated a hidden trap and fall into a deep hole to your death\n GAME OVER.")



