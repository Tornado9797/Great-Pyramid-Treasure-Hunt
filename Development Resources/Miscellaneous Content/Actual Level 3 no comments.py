#Level 3 Legit
#(the actual level 3)

#These are here just to make the program work and are not to be copy-pasted

inventory=[]
health=100

import random

#Copy-paste starting here
def puzzle_lines():
    print("\n|___|___|___|___|")
    print("|   |   |   |   |")
    print("| ", end="")

def display_puzzle(letters):
    print(" ___ ___ ___ ___ ")
    print("|   |   |   |   |")
    print("|", end=" ")

    for i in range(2):
        for i in range(i*4,(i*4)+4):
            print(letters[i],"|", end=" ")
        puzzle_lines()

    for i in range(8,12):
            print(letters[i],"|", end=" ")
        
    print("\n|___|___|___|___|")

def level_3(inventory, health):
    door="n"
    trip="n"
    wall="n"
    floor="n"

    puzzle1=["a","b","c","d","a","b","c","d","a","b","c"," ",
            "this","serves","to lengthen","the list"]
    puzzle2=["a","b","c","d","a","b","c"," ","a","b","c","d",
            "this","serves","to lengthen","the list"]
    puzzle3=["a","b","c"," ","a","b","c","d","a","b","c","d",
            "this","serves","to lengthen","the list"]
    puzzle4=[" ","c","b","a","d","c","b","a","d","c","b","a",
            "this","serves","to lengthen","the list"]
    puzzle5=["d","c","b","a"," ","c","b","a","d","c","b","a",
            "this","serves","to lengthen","the list"]
    puzzle6=["d","c","b","a","d","c","b","a"," ","c","b","a",
            "this","serves","to lengthen","the list"]

    print(
        """
    You enter the room.

    There is a piece of parchment on the east wall, and something metal on the
    west wall glints in the beam of your flashlight.
        """
        )

    while door=="n":
        user=input("\n>")
        user=user.lower()
    
        if (user=="look around" or user=="look"):
            print("There is a piece of parchment on the east wall, and something")
            print("metal on the west wall glints in the beam of your flashlight.")
            if wall=="y":
                print("\nIn the hidden room, there is an odd assortment", end=" ")
                print("of tiles on the wall.")

        elif (user=="inspect floor" or user=="look at floor"):
            floor="y"
            if trip=="y":
                print("\nYou search for the thing", end=" ")
                print("that caused you to stumble earlier.")
                print("What you find astonishes you: an oddly modern screwdriver.")
            else:
                print("\nCurious about what might be on the floor,", end=" ")
                print("you look by flashlight.")
                print("What you find astonishes you:", end=" ")
                print("a strangely modern screwdriver.")
        
        elif (user=="pick up screwdriver" or user=="add screwdriver to inventory"
              or user=="acquire screwdriver" or user=="take screwdriver"):
            if (trip=="n" and floor=="n"):
                print("What screwdriver?")
            else:
                print("\nYou pick up the screwdriver and put it in your pocket.")
                inventory+=["screwdriver"]

        elif (user=="inspect parchment" or user=="read parchment"
              or user=="inspect east wall" or user=="look at east wall"):
            if ("screwdriver" not in inventory and trip=="n"):
                print("\nOn your way to the wall, you trip over something")
                print("small and cyclindrical, and scrape your knee.")
                print("It rolls away before you can get a good look at it.")
                print("Frustrated, you turn back towards the parchment.")
                health-=5
                trip="y"
            print("\nThe parchment reads:")
            print("\nyou Will hAve to Sort your mAil to keep", end=" ")
            print("it from blocking the Door.")
            print("wisdom is necessary for escape.")

        elif (user=="look at west wall" or user=="inspect west wall" or
              user=="inspect metal"):
            if "screwdriver" not in inventory and trip=="n":
                print("\nOn your way to the wall, you trip over something")
                print("small and cyclindrical, and scrape your knee.")
                print("It rolls away before you can get a good look at it.")
                print("Frustrated, you turn back towards the wall.")
                health-=5
                trip="y"
            print("\nYou walk to the west wall.  There is a")
            print("screw drilled into the stone bricks.  You wonder")
            print("what a modern screw is doing in an ancient pyramid.")

        elif (user=="unscrew screw" or user=="take screw"):
            if "screwdriver" in inventory:
                print("\nYou unscrew the screw, but something", end=" ")
                print("happens that you don't expect.")
                print("The screw was attached to a string.", end=" ")
                print("A weight shifts off of a scale,")
                print("and something comes crashing into the wall, knocking it down.")
                print("Another room is revealed.")
                wall="y"
                print("\nUnfortunately for you, a piece of rubble", end=" ")
                print("hits you on the head.")
                health-=20
                print("After rubbing your head, you decide that one such rock")
                print("might be effective against enemies- if there were any.")
                print("You pick up a chunk of stone and try to put")
                print("it in your pocket, but sadly, it does not fit.")
                print("You settle with carrying the rock in your other hand.")
                inventory+=["rubble"]
            else:
                print("\nYou try to take the screw out with your fingernail,")
                print("but it breaks.  Mildly annoyed,", end=" ")
                print("you turn away from the wall.")
                health-=2

        elif (user=="inspect tiles" or user=="solve puzzle"):
            if wall=="n":
                print("\n...what?  There's nothing to see here!")
                continue
            space=11
            times=0
            wisdom="n"
            direct=""
            letters=["c","b","c","d","b","d","a","c","a","b","a"," ",
                     "this","serves","to lengthen","the list"]
            display_puzzle(letters)

            print("\nThe tiles appear to be some sort of puzzle.")
    
            while ((letters!=puzzle1 and letters!=puzzle2 and letters!=puzzle3
                    and letters!=puzzle4 and letters!=puzzle5 and letters!=puzzle6)
                    and (wisdom=="n")):
                direct=input("\n>")
                if (direct=="left" or direct=="l" or direct=="a"):
                    if (space!=0 and space!=4 and space!=8):
                        letters[space]=letters[space-1]
                        letters[space-1]=" "
                        space-=1
                        display_puzzle(letters)
                        times+=1
                    else:
                        display_puzzle(letters)
                        continue
                elif (direct=="right" or direct=="r" or direct=="d"):
                    if (space!=3 and space!=7 and space!=11):
                        letters[space]=letters[space+1]
                        letters[space+1]=" "
                        space+=1
                        display_puzzle(letters)
                        times+=1
                    else:
                        display_puzzle(letters)
                        continue
                elif (direct=="up" or direct=="u" or direct=="w" or direct=="top"):
                    if ((space-4)>-1):
                        letters[space]=letters[space-4]
                        letters[space-4]=" "
                        space-=4
                        display_puzzle(letters)
                        times+=1
                    else:
                        display_puzzle(letters)
                        continue
                elif (direct=="down" or direct=="d" or direct=="s" or direct=="bottom"):
                    if ((space+4)<12):
                        letters[space]=letters[space+4]
                        letters[space+4]=" "
                        space+=4
                        display_puzzle(letters)
                        times+=1
                    else:
                        display_puzzle(letters)
                        continue
                elif (direct=="wisdom" or direct=="Wisdom"):
                    wisdom="y"
                else:
                    display_puzzle(letters)
            if (letters==puzzle1 or letters==puzzle2 or letters==puzzle3
                or letters==puzzle4 or letters==puzzle5 or letters==puzzle6):
                print("\nIt took you", times, "moves to solve the puzzle.")
                print("(in case you were interested)")
                print("\nThe door slowly creaks open to reveal another staircase.")
            elif (direct=="wisdom" or direct=="Wisdom"):
                print("\nYou step away from the puzzle.")
            else:
                print("\nIt seems the gods of the pyramid are conspiring against you.")
                print("You decide to try again later.")

        elif (user=="climb stairs" or user=="climb staircase" or user=="ascend"):
            print("\nYou cautiously ascend the dark stairs.")
            door="y"

        elif (user=="pick up rubble" or user=="pick up rock"
              or user=="acquire rubble" or user=="acquire rock"):
            print("You pick up a chunk of stone and try to put")
            print("it in your pocket, but sadly, it does not fit.")
            print("You settle with carrying the rock in your other hand.")
            inventory+=["rubble"]  

        elif user=="health":
            print("Your health:",health)
    
        elif user=="inventory":
            print("Your inventory:")
            for element in inventory:
                print(" -", element)

        else:
            number=random.randint(1,3)
            if number==1:
                print("\n\"", user, "!\" you swear, angry at the pyramid.")
            if number==2:
                print("\nYou know, \"", user, "\"could be the")
                print("first line of your autobiography.")
            else:
                print("\n\"", user, "!\" you shout, hoping in")
                print("vain that it's a password of some sort.")

    input("\n\nPress the enter key to exit.")

    return health
    return inventory

level_3(inventory, health)

input("Press the enter key to exit.")
