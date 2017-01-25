#Level 4
#(that one level with the fan)

import random

health=100
inventory=["screwdriver","rubble","parchment"]

def level_4(health, inventory):
    print("\tYou ascend the staircase deliberately, rubbing your head.")
    print("\tYou know that there will be a bump there tomorrow.")

    door="n"
    fanblades=False
    wind_tunnel_deep=False
    wind_tunnel_shallow=False
    grille_deep=True
    grille_shallow=True
    fan_placement="wall"
    fan_power=True

    while (door=="n" and health>0):
        if (wind_tunnel_deep==True and wind_tunnel_shallow==True):
            print("The hidden door between the two grilles opens,")
            print("revealing a staircase.")

        if health<1:
            print("GAME OVER")
            break

        user=input("\n>")
        user=user.lower()

        if user in ("look", "look around"):
            print("\nThere are two holes in the south wall,", end=" ")
            print("but you can’t see them very well.")
            print("There is also a large tapestry on the north wall.")
            print("There is a faint humming sound in the air,")
            print("almost like the turning of a small motor.")
            print("But you know that can’t be.")
            print("This pyramid is at least two thousand years old...")

        elif user in ("look at wall", "inspect south wall", "inspect wall",
                      "inspect holes"):
            print("\nThere are two holes in the wall, both very deep.")
            print("The one on the left is deeper than the one on the right.")
            print("Both are covered by metal grilles screwed into the wall.")
            print("You see a red flashing light at the end of each.", end=" ")
            print("Sensors perhaps?")
            print("By now you are used to finding modern technology")
            print("in the pyramid and don't find this suspicious.")

        elif user in ("listen","inspect motor","inspect air"):
            print("\nThe humming sound is coming from the east wall.")

        elif user in ("inspect east wall", "inspect humming sound"):
            print("\nIn the dark, you almost don't see the fan.")
            print("Or at least, you come to the conclusion that the")
            print("rapidly rotating rod on a stand is a fan without blades.")
            print("But how could it still be running?")
            print("You wonder if there are continuity errors in", end=" ")
            print("your own expedition.")

        elif user in ("inspect north wall", "inspect tapestry"):
            print("\nThere is a detailed tapestry hanging on the wall.")
            print("You decide that the odd scene it depicts is a grand")
            print("royal council made of inhuman figures.")

        elif user in ("pull back tapestry", "remove tapestry", "take tapestry"):
            print("\nYou decide you like this tapestry and its inhuman figures.")
            print("You put it in your pocket, not sure of how you are", end=" ")
            print("able to do so.")
            print("Stuck behind the tapestry are three fan blades.")
            inventory+=["tapestry"]

        elif user in ("take blades", "take fan blades"):
            inventory+=["fan blades"]
            print("\nYou put the fan blades in your pocket with the tapestry,")
            print("now very aware of continuity errors.")

        elif user in ("inspect fan"):
            print("\nYou wonder how the fan has remained spinning all these years.")
            print("Unless perhaps the ancients didn't leave so long ago.")
            if fan_power==True:
                fan_power=False
                print("\nYou find a blue button at the base of the,", end=" ")
                print("fan, and push it, turning the fan off.")
            else:
                fan_power=True
                print("\nYou find a blue button at the base of the,", end=" ")
                print("fan, and push it, turning the fan on.")

        elif user in ("push button"):
            if fan_power==True:
                fan_power=False
                print("\nYou push the button, turning the fan off.")
                if fan_placement=="deep":
                    print("\nThe sensor light blinks once, and")
                    print("you hear another click from behind the wall.")
                    wind_tunnel_deep=False
                elif fan_placement=="shallow":
                    print("\nThe sensor light blinks once, and")
                    print("you hear another click from behind the wall.")
                    wind_tunnel_shallow=False
                    print("But what did the riddle say again?")
            else:
                fan_power=True
                print("\nYou push the button, turning the fan on.")
                if fan_placement=="deep":
                    print("\nThe sensor blinks twice, and")
                    print("you hear a click from behind the wall.")
                    wind_tunnel_deep=True
                elif fan_placement=="shallow":
                    print("\nThe sensor blinks twice, and")
                    print("you hear a click from behind the wall.")
                    wind_tunnel_shallow=True
                    print("But what did the riddle say again?")

        elif user in ("attach blades","use blades","attach fan blades",
                      "use fan blades","insert fan blades","insert blades",
                      "build fan"):
            if "fan blades" in inventory:
                if fan_power==True:
                    print("\nYou decide that doing this while the fan is")
                    print("still running is not a good idea.")
                else:
                    print("\nYou slide the blades into three slots on the rod.")
                    inventory.remove("fan blades")
            else:
                print("\nYou don't have any blades to attach.")

        elif user in ("acquire fan","take fan","pick up fan"):
            if fan_power==False:
                inventory+=["fan"]
                print("\nYou put the fan in your pocket with", end=" ")
                print("the equally large tapestry.")
                print("How exactly you do this is unknown to you.")
                fan_placement="inventory"
            else:
                print("\nYou decide that putting a spinning fan in your pocket")
                print("might shred that lovely tapestry and decide against it.")

        elif user in ("use fan","put down fan","place fan","move fan"):
            fan_placement=input("\nWhere? ")
            if fan_placement in ("deep","deep tunnel", "left hole",
                                 "left tunnel","deeper tunnel"):
                print("\nYou place the fan in front of the deeper tunnel.")
                fan_placement="deep"
                inventory.remove("fan")
                if fan_power=True:
                    print("\nThe sensor blinks twice, and")
                    print("you hear a click from behind the wall.")
                    wind_tunnel_deep=True
            elif fan_placement in ("shallow", "shallow tunnel", "right tunnel",
                                   "right hole"):
                print("\nYou place the fan in front of the shallow tunnel.")
                fan_placement="shallow"
                inventory.remove("fan")
            else:
                print("\nYou decide that those tunnels have got to do something.")

        elif user in ("use screwdriver", "unscrew grille",
                      "unscrew right grille", "unscrew grilles",
                      "unscrew screws"):
            grille=input("\nRemove which grille? ")
            if grille in ("left grille", "deep", "deep tunnel","left"):
                if "left grille" not in inventory:
                    print("\nYou use your screwdriver to remove the", end=" ")
                    print("grille on the deeper tunnel.")
                    inventory+=["left grille"]
                else:
                    print("\nYou raise your screwdriver to do so, but then")
                    print("remember that you already have the grille in your pocket.")
                    if fan_placement=="inventory":
                        print("...with the tapestry.  And the fan.")
                grille_deep=False
            elif grille in ("right grille","shallow","shallow tunnel","right"):
                if "right grille" not in inventory:
                    print("\nYou use your screwdriver to remove the", end=" ")
                    print("grille on the shallow tunnel.")
                    inventory+=["right grille"]
                else:
                    print("\nYou raise your screwdriver to do so, but then")
                    print("remember that you already have the grille in your pocket.")
                    if fan_placement=="inventory":
                        print("...with the tapestry.  And the fan.")
                grille_shallow=False

        elif user in ("throw rock", "throw rubble", "use rubble", "use rock",
                      "place rubble", "place rock"):
            print("\nIf those blinking lights are indeed sensors,")
            print("what if one were to break?")
            print("\nYou decide that the shallower tunnel is your best bet.")
            if grille_shallow==False:
                print("\nYou launch the rock towards the light.")
                print("It has the same effect on the sensor as", end=" ")
                print("it did on your head.")
                print("You hear a click from behind the wall.")
                wind_tunnel_shallow=True
                inventory.remove("rubble")
            else:
                print("But unfortunately, it is covered by a grille.")

        elif user in ("read parchment", "read riddle"):
            print("\nYou take the parchment out of your ever-expanding pocket.")
            print("It reads:")
            print("\neArth beAtS WinD")
            print("WisDom is neceSSAry for eScApe.")

        elif user in ("ascend stairs", "climb stairs", "climb staircase"):
            print("You cautiously walk up the stairs.")
            door="y"
            break

        elif user=="wisdom":
            print("\nYou decide to stop breaking the fourth wall, unaware that")
            print("by doing this, you have broken the fourth wall again.")

        elif user=="health":
            print("\nYour health:",health)
    
        elif user=="inventory":
            print("\nYour inventory:")
            for element in inventory:
                print(" -", element)

        else:
            number=random.randint(1,3)
            if number==1:
                print("\n\"", user, "!\" you swear, angry at the pyramid.")
            elif number==2:
                print("\nYou know, \"", user, "\" should be the")
                print("first line of your autobiography.")
            else:
                print("\n\"", user, "!\" you shout, hoping in")
                print("vain that it's a password of some sort.")

    print("LEVEL END")

    if health<1:
        print("(sorry about that)")
    else:
        print("The door shuts behind you with a snap.")

    return health, inventory

level_4(health, inventory)

print("\nYour health:",health)

print("\nYour inventory:")
for element in inventory:
    print(" -", element)

input("Press the enter key to exit.")

#unscrew grilles
#inspect east wall (fan)
#inspect north wall (tapestry)
#pull back tapestry
#take blades
#attach blades
#inspect fan
#push button on fan
#acquire fan
#place fan
#throw rock
#climb stairs
