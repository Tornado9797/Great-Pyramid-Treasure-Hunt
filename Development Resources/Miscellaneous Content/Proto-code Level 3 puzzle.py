#The Great Pyramid Treasure Hunt
#Level 3 - Puzzle Door

#Displaying the Puzzle
def puzzle_lines():
    print("\n|___|___|___|___|")
    print("|   |   |   |   |")
    print("| ", end="")

def display_puzzle(puzzle):
    print(" ___ ___ ___ ___ ")
    print("|   |   |   |   |")
    print("|", end=" ")

    for i in range(3):
        for i in range(i*4,(i*4)+4):
            print(puzzle[i],"|", end=" ")
        puzzle_lines()

    for i in range(12,16):
            print(puzzle[i],"|", end=" ")
        
    print("\n|___|___|___|___|")

#Moving Tiles
        space=11
        times=0
        wisdom="n"
        direct=""
        letters=["c","b","c","d","b","d","a","c","a","b","a"," ",
                 "this","serves","to lengthen","the list"]
        display_puzzle(letters)

        print("The tiles appear to be some sort of puzzle.")
if space==11:  #not important, I just didn't feel like deleting tabs
    if space==11:
        while ((letters!=puzzle1 and letters!=puzzle2 and letters!=puzzle3
                and letters!puzzle4 and letters!=puzzle5 and letters!=puzzle6)
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
            print("\nIt seems the gods of the pyramid are conspiring", end=" ")
            print("against you.")
            print("You decide to try again later.")

input("\n\nPress the enter key to exit.")
            
