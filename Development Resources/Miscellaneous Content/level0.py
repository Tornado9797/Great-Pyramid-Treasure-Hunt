# prelude

def introduction():
    enter = False
    health = 100
    inventory = ['flashlight']
    print("Welcome to the Graeat Pyramid Treasure Hunt.\n\n",
          "You are a world renowned treasure hunter who has traveled\n",
          "thousands of miles to this mysterious and exotic location\n",
          "in search of riches and glory.\n\n",
          "To control your character, type SIMPLE commands into the prompt.\n",
          "The computer will only understand simple commands, so try\n",
          "to be as brief as possible. For example, instead of typing\n",
          "'LOOK AT THE DOOR', you might try 'INSPECT DOOR', and instead\n",
          "of 'PICK UP THE ROCK AND PUT IN POCKET', you might try 'TAKE ROCK'\n"
          "Try LOOKing around for a start.")

    print("\nFor a list of some generic commands, type 'help' before\n",
          "you enter the pyramid and begin your adventure.\n")
    while not enter:
        action = input("\n> ")
        action = action.lower()
        if action == 'inventory':
            print(inventory)
        elif action == 'help':
            print("If you are stuck, try the following commands:")
            print("\nLOOK\nOPEN\nINSPECT\nREAD\nUSE\nGIVE\nTAKE",
                  "\nSome of these will requre an object in conjunction with the command",
                  "\n\nYou may be able to do other simple things in",
                  "certain situations")
        elif action == 'health':
            print(health)
        elif action == 'look':
            print("\nIn front of you looms a gigantic, ancient pyramid.\n",
                  "A huge set of double doors dominates the face of the\n",
                  "pyramid. Somthing appears to be carved above the doors.")
        elif action == 'inspect pyramid':
            print("\nThe pyramid is made of smooth stone. Apart from it's\n",
                  "monstorous size and large entrance, there is nothing\n",
                  "particularly interesting about it")
        elif action in ('inspect doors', 'inspect door', 'inspect entrance'):
            print("\nTaking a closer look, you notice that there is no\n",
                  "lock or other barrier on the doors. It is now clear\n",
                  "that the carvings above are a poem of some sort.")
        elif action in ('inspect carving','inspect carvings','inspect poem','read poem'):
            print("\nThe carving is in a language you do not recognize.\n",
                  "After staring at the characters for some time,\n",
                  "they morph into English")
            print("It reads")
            print("\t\tGo away.")
        elif action in ('open door','enter pyramid','open doors'):
            enter = True
            print("\nYou give the door a tug. It's a rather heavy door. But\n",
                  "it swings open easily enough.")
        elif action == 'cheat':
            print("You win")
            enter = True
    return health,inventory


health,inventory = introduction()
input("Press the enter key to exit")
                  
                  
                  
                  
