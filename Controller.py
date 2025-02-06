import CPSS_System
import Globals
# The controller should be the main glue between all the other py modules.

# ----------------------------------------------
# Main Controller
# ----------------------------------------------


def mainMenu():
    run = True
    while run:
            # Preamble and initial option selection
            print("----------------------------------------")
            print("What would you like to do?")
            print("----------------------------------------")
            print("(1) See consequence data")
            print("(2) See subsystems within larger system")
            print("(3) Get general system information")
            print("(4) Graph output of system STRETCH GOAL")
            print("(B) Back ")
            queryData= input("Choose Option: ")
            print("You Selected " + queryData)
            
            if queryData == "1":
                menu_1_ConsequenceData()
            elif queryData == "2":
                print("ff")
            elif queryData == "3":
                print("hh")
            elif queryData == "4":
                print("gg")

            elif queryData == "B" or queryData == "b":
                return 
            else:
                print("Error with setup option selected. Try again")

            print("----------------------------------------")

def menu_1_ConsequenceData():
    print("----------------------------------------")
    print(" See Consequence Data")
    print("----------------------------------------")
    # Collect inputs
    node= input("Give System Name for query: ")
    print("Your input: " + node)
    number= input("Give Number of Orders of Consequence: ")
    print("You input: " + number)
    # Data check
    # Later?

    # Convert input string to integer
    number=int(number)

    # Calsulate consequences
    myNode = Globals.systemList[node]
    consequences = myNode.queryConsequences(myNode, number,0)

    # Format for output
    updatedConsequenceList = {}

    count = 1
    for key, value in consequences.items():
        if len(value) != 0 and count <= number:
            temp = value[0]
            updatedConsequenceList[key] = temp.sysName
        count = count + 1
    # Print output
    print(f'Consequences of an outage at node {node} are:\n{updatedConsequenceList}\n')
    print("----------------------------------------")
