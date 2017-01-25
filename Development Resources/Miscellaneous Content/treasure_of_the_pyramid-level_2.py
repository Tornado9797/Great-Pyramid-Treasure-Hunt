# Conner Joseph Brewster
# Tuesday, Decemeber 10th, 2013 @ 2:55:28 PM Central Standard Time (Not Daylight Savings Time)
# Pre-AP Computer Science
# Annette Walter - 7th Period

# Treasure of the Pyramid
# Level 2 Beta

# CAUTION: Program does not run in Interactive Mode.

health = 100
inventory = ["Flashlight", "Key"]
win = False
ending_statement = False
def level2(health, inventory):
    print("The room you have entered seems to be smaller\nand a little brighter than the previous one…")
    exit_room = False
    no_mirror = False
    no_lock = False
    no_bush = False
    eyes = 2
    while (exit_room == False and health > 1):
        choice = input("\nAction: ")
        choice = choice.lower()
        if choice == "nope":
            print("You decide that you are a rabid monkey. You charge head first into the wall.\nNot surprisingly, it makes a loud clank and you fall in pain.")
            health -= 25
        elif choice == "inventory":
            print("You have", inventory, "in your pockets.")
        elif choice == "explode":
            print("You blew up.")
            break
        elif choice in ["throw flashlight", "hurl flashlight", "fling flashlight"]:
            print("You blindly hurl your flashlight upwards without looking.\nIt merely lands on your head with a thud. No blood clot occurs, but it hurts.\nYou wonder how you made it this far in life while\nmaking decisions similar to that.\nYou place the flashlight back in your pockets.")
            health -= 5
        elif choice in ["throw key", "hurl key", "fling key"]:
            print("You blindly hurl your key upwards without looking.\nIt merely lands in your eye. You now cannot see out of that eye.\nSeriously?\nYou place the key back in your pockets.")
            eyes -= 1
            health -= 5
            if eyes == 0:
                print("\nYou are now completely blind.\nDidn't you learn from the first time you threw your keys that\nit was a bad idea?")
                break
        elif choice in ["throw mirror", "hurl mirror", "fling mirror"]:
            if "Mirror" in inventory:
                print("You blindly hurl your mirror upwards without looking.\nIt slams into your skull and shatters. It hurts, and the mirror is completely destroyed.")
                del inventory [2]
                health -= 10
        elif choice in ["look at flashlight", "inspect flashlight"]:
            print("You take a closer look of the flashlight.\nTurns out... it's a flashlight.\nGo figure.")
        elif choice == "health":
            print("You examine your health count\n(because health can be read as a percentage these days)\nto be", health,"%.")
        elif choice == "take pyramid":
            print("You clutch the ground beneth you and stuff the\npyramid in your pocket.\nHowever, since you are inside of the pyramid, you also go in your pockets,\nHowever, since your pyramid is in your pocket of you who is inside the pyramid and\naiwdhapIDHiahdipuahdpihdpahdiphdpaodjoadjpoajpdjpjdiebhfouehfehfuioefhaeufh08wq34hy0897523y90823ynv08732nf89y3v07283vb87vn327cf897c7829379`0010101010100101-0101010101001010101001010100101010100101")
            break
        elif choice == "open flashlight":
            if "screwdriver" in inventory:
                print("Impossible.")
                break
            else:
                print("You are unable to open the flashlight,\na proper tool is required.")
        elif choice == "look":
            print("\nYou find a dusty mirror hanging angled on the left wall,\nsome hieroglyphics to the right,\na red box left of that,\nand dense thorny bushes.")
            choice = input("\nAction: ")
            choice = choice.lower()
        elif choice in ["look in mirror", "see mirror", "examine mirror", "inspect mirror"]:
            if no_mirror == False:
                print("Inside the relection you see yourself, looking more sexy than ever.\n...and a dark object approaching you at an incredible rate.\nBefore you could react, you are whisked away.\nYou wake up on the previous floor with no sign of the creature.")
                print("\nBecause the creature doesn't have a degree in\ntransportation safety, you are hurt.")
                health -= 10
                level1(health, inventory)
            else:
                print("For some reason the mirror cannot be seen inside anymore.\nIt just looks like a slab of bronze.")
        elif choice in ["take mirror", "acquire mirror", "steal mirror", "grab mirror"]:
            if no_mirror == False:
                print("Without looking inside you detach the mirror\nfrom the wall and put it in your pocket…\nhow the heck did you do that?")
                inventory += ["Mirror"]
                no_mirror = True
                print("\nBehind where the mirror was lies some text.\nOddly enough, it's in English lettering.")
                print("\nIt reads: htiw detrats yeht tahw esol tsum eno ,htrae detaeh eht nihtiw")
            else:
                print("\nYou look at the text once more...")
                print("\nIt reads: htiw detrats yeht tahw esol tsum eno ,htrae detaeh eht nihtiw")
        elif choice in ["look at hieroglyphics", "inspect hieroglyphics"]:
            print("You translate the text...\n\nIT.. IT DON GIV MERCI NO LOOKIE\n\nYou then wonder why the text looks smeared in\na bloody red...")
        elif choice in ["take red box", "acquire red box", "steal red box", "grab red box"]:
            print("You grab the box and lift it up\nspikes pop out from the sides of the box and pierce you.\nIn instinct, you drop the box...\nright on top of your foot.\nYour cries of agony echo loudly throughout the room.")
            health -= 20
        elif choice in ["inspect red box"]:
            print("You take a closer look at the red box...\nIt seems out of place, a little modern for an ancient pyramid.")
            if no_lock == False:
                print("You see that it is tightly shut with a key lock in place.")
            else:
                print("You see the place where the Flint and Steel once rested.")
        elif choice == "use key":
                    print("With a quick click, the red box's lid pops off.\nWithin you find a Flint and Steel. You grab it.")
                    no_lock = True
                    inventory += ["Flint and Steel"]
        elif choice in ["look at thorns", "inspect thorns"]:
            print("You step closer to the dense bushes.\nYou feel nervous around their incrediblly sharp thorns.\nAt the end you see a light shimmering from inside.")
        elif choice in ["enter thorns", "go in thorns"]:
            if no_bush == True:
                print("You easily slide through the bushes.\n\nYou find yourself in front of a ladder. You climb it.")
                print("\n\n\n@trigger Level 3")
                win == True
                break
            else:
                print("You attempt to push through the bushes,\nbut you are severely wounded from the sharp thorns.\nYou retreat back for now into the main area.")
                health -= 10
        elif choice in ["ignite flint and steel", "use flint and steel"]:
            if "Flint and Steel" in inventory:
                print("You immediately trigger your Flint and Steel\nwhich happens to be in your pocket.\nAn intense burning follows, resulting in singed pants.")
                health -= 25
            else:
                print("What Flint and Steel?")
        elif choice in ["burn thorns", "ignite flint and steel on thorns", "use flint and steel on thorns"]:
            if "Flint and Steel" in inventory:
                print("You go near the bushes and light the Flint and Steel.\nThe thorns disappear without a trace.")
                no_bush = True
            else:
                print("What Flint and Steel?")
        else:
            print("You scream", choice,"hoping that it is some sort of password.")
level2(health, inventory)
while ending_statement == False:
    if win == False:
        print("\n\nYou begin to grow dizzy and fall to the ground in death.")
        print("\n\nGAME OVER!")
        ending_statement = True
    else:
        print("\n\nYou have entered level 3")
        ending_statement = True
input("\n\nPress the enter key to exit.")
