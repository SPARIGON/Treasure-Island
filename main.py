print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You are standing at a crossroads in a dark forest.")

choice_1 = input("Do you want to go LEFT towards the faint sound of running water or RIGHT towards the eerie glow? \n").upper()

if choice_1 == "LEFT":
    print("You follow the sound and arrive at a riverbank.")
    choice_2 = input("Do you SWIM across the river or WAIT for a safer way to cross? \n").upper()

    if choice_2 == "WAIT":
        print("After waiting for a while, a mysterious boatman offers you a ride across the river.")
        choice_3 = input("Once across, you find three doors in a clearing. Which door do you choose? YELLOW, RED, or BLUE? \n").upper()

        if choice_3 == "YELLOW":
            print("You open the yellow door and find a treasure chest filled with gold and jewels. You WIN!")
        elif choice_3 == "RED":
            print("You open the red door and are engulfed in flames. Burned by fire.\nGame Over.")
        elif choice_3 == "BLUE":
            print("You open the blue door and are devoured by a pack of wild beasts. Eaten by beasts.\nGame Over.")
        else:
            print("Invalid choice. Lost in the forest.\nGame Over.")
    else:
        print("As you swim across the river, you are attacked by a swarm of piranhas. Attacked by trout.\nGame Over.")
else:
    print("You follow the eerie glow and fall into a hidden pit. Fall into a hole.\nGame Over.")