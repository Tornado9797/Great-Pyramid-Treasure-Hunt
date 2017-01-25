
health = 100
inventory = []
def level_1(health, inventory):
    print("You step into a huge room. The door swings shut behind you.")
    exit_room = False
    door = 'locked'
    sarcophagus = ['medalion', 'key', 'closed']
    while not exit_room:
        action = input("\n> ")
        action = action.lower()
        if action == 'inventory':
            print(inventory)
        elif action == 'health':
            print(health)
        if action == 'look':
            print("\nThe room you are in is very large and bare.\n",
                  "Directly in front of your there is another door,\n",
                  "much smaller than the first. To you left, there is\n",
                  "a long sarcophagus.")
        elif action == 'inspect door':
            print("\nNext to the door, a skeleton hand protrudes from the wall.\n",
                  "Above the hand, you see the enscription:\n",
                  "\t\t'Tribute'")
        elif action == 'open door':
            if door == 'locked':
                print("\nThe door is locked.")
            elif door == 'unlocked':
                door = 'open'
                print("\nThe door swings open easily, revealing a staircase leading up.")
            else:
                print("Door opened.")
                door = 'open'
        elif action == 'inspect hand':
            print("\nThere is nothing particularly interesting about\n",
                  "the hand. It looks as if it is waiting for somthing")
        elif action == 'inspect sarcophagus':
            print("\nThe sarcophasgus is very elaborate. it is plated\n",
                  "in gold and jewels. On the lid, the words 'A theif's reward'\n",
                  "appear")
        elif action in ('open sarcophagus','lift lid'):
            if 'closed' in sarcophagus:
                sarcophagus.remove('closed')
            if 'medalion' in sarcophagus and 'key' in sarcophagus:
                print("\nThe lid creaks open. Inside there is an ancient\n",
                      "mummy. Arround the mummy's neck there is a\n",
                      "gold medalion. A small metal key lies next to the mummy")
            elif 'medalion' in sarcophagus:
                print("\nThe lid creaks open. Inside there is an ancient\n",
                      "mummy. Arround the mummy's neck there is a\n",
                      "gold medalion.")
            elif 'key' in sarcophagus:
                print("\nThe lid creaks open. Inside there is an ancient\n",
                      "mummy. A small metal key lies next to the mummy")
            else:
                print("\nThe lid creaks open. Inside there is an ancient\n",
                      "mummy.")
        elif action == 'take medalion':
            if 'medalion' in sarcophagus and 'closed' not in sarcophagus:
                sarcophagus.remove('medalion')
                inventory.append('medalion')
                print("\nYou have added the medalion to your inventory.")
            elif 'medalion' in inventory:
                print("\nYou already have this item.")
        elif action == 'take key':
            if 'key' in sarcophagus and 'closed' not in sarcophagus:
                sarcophagus.remove('key')
                inventory.append('key')
                print("\nYou have added the key to your inventory.")
            elif 'medalion' in inventory:
                print("You already have this item.")
        elif action in ('give medalion', 'place medalion'):
            if 'medalion' in inventory:
                door = 'unlocked'
                print("\nYou cautiously drop the medalion into the skeleton's hand.\n",
                      "The bony fingers crack as they close arround the gold. You\n",
                      "hear a light click behind the door")
        elif action in ('give key', 'place key'):
            if 'key' in inventory:
                print("\nNothing happens. You slide the key back into your pocket")
        elif action == 'shake hand':
            health -= 10
            print("\nYou clasp the skeleton's hand. Suddenly its grip hardens\n",
                  "and you cannot break free. You struggle against the hand.\n",
                  "It loosens its grip and you fall backwards, striking your\n",
                  "head on the stone floor.\n(health - 10)")
        elif action in ('climb stairs', 'climb staircase', 'enter door'):
            if door == 'open':
                print("\nYou ascend the stairs to the next level.")
                exit_room = True
            elif door == 'unlocked':
                print("\nThe door is still closed.")
            else:
                print("\nThe door is locked.")

    return health,inventory
        
       
            
health,inventory = level_1(health, inventory)
input("Press the enter key to exit.")
