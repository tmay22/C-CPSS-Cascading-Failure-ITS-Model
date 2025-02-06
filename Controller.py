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
            print("(3) Print system key data")
            print("(4) Graph output of system STRETCH GOAL")
            print("(B) Back ")
            queryData= input("Choose Option: ")
            print("You Selected " + queryData)
            
            if queryData == "1":
                menu_1_ConsequenceData()
            elif queryData == "2":
                menu_2_SubSystems()
            elif queryData == "3":
                menu_3_SystemKeyData()
            elif queryData == "4":
                print("gg")

            elif queryData == "B" or queryData == "b":
                return 
            else:
                print("Error with setup option selected. Try again")

            print("----------------------------------------")

def menu_1_ConsequenceData():
    print("----------------------------------------")
    print("See Consequence Data")
    print("----------------------------------------")
    # Collect inputs
    node=input("Give System Name for query: ")
    print("Your input: " + node)
    number= input("Give Number of Orders of Consequence: ")
    print("You input: " + number)
    # Data check
    # Later?
    print("----------------------------------------")
    # Convert input string to integer
    number=int(number)

    # Calsulate consequences
    myNode = Globals.systemList[node]
    consequences = myNode.queryConsequences(number,0)

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
    

# See SubSystems within Larger Systems
def menu_2_SubSystems():
    print("----------------------------------------")
    print("See SubSystems within Larger Systems")
    print("----------------------------------------")
    # Collect inputss
    node=input("Give SubSystem Name for Query: ")
    print("Your input: " + node)
    print("----------------------------------------")
    nodeObj = Globals.systemList[node]
    
    inputs = nodeObj.primaryInputs
    processes = nodeObj.primaryProcesses
    outputs = nodeObj.primaryOutputs

    inputList = []
    processList = []
    outputList = []

    for inp in inputs:
        inputList.append(inp.sysName)
    for processs in processes:
        processList.append(processs.sysName)
    for outp in outputs:
        outputList.append(outp.sysName)
    # Print output
    print(f'Subsystem components within system: {node}\nInputs: {inputList}\nProcesses: {processList}\nOutputs{outputList}\n')
  

# See SubSystems within Larger Systems
def menu_3_SystemKeyData():
    print("----------------------------------------")
    print("Print System Key Data")
    print("----------------------------------------")
    # Collect inputss
    node=input("Give SubSystem Name for Query: ")
    print("Your input: " + node)
    print("----------------------------------------")
    nodeObj = Globals.systemList[node]
    
    sysName = nodeObj.sysName
    isCyber = nodeObj.isCyber
    isPhysical = nodeObj.isPhysical
    isSocial = nodeObj.isSocial
    degree = nodeObj.degree
    directlyAffects = nodeObj.affectorList
    dAffects = []
    for obj in directlyAffects:
        dAffects.append(obj.sysName)
    

    # Print output
    print(f'Key data for {node}\nCyber: {isCyber} | Physical: {isPhysical} | Social: {isSocial}')
    print(f'Node degree: {degree}')
    print(f'Node directly affects: {dAffects}')
  
