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

#Write your code below this line 👇

first_choice = input("You're at a crossroads, where do you want to go: left (l) or right (r)?")

if first_choice == 'l':
    print("Great Choice! You just avoided an asteroid.")
    second_choice = input("You reach a river, do you want to swim (s) across or wait (w) for a boat?")
    if second_choice == 'w':
        print("Way to go! You just avoided getting eaten by hungry crocodiles.")
        third_choice = input("You find a house with three doors, red (r), blue (b) and green (g). Which door you pick?")
        if third_choice == 'r':
            print("Hooray! You found the treasure!")
        elif third_choice == 'b':
            print("Oh no! You just got imprisoned by a fiery dragon.")
        else:
            print("Oh no! You just fell into an infinite hole.")
    else:
        print("Yikes! You just got eaten by hungry crocodiles.")
else:
    print("Oops! You just got hit by an asteroid.")

