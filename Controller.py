import CPSS_System
import Globals
import Graph
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
            print("(1) See consequence of Outage and Cascading Failure data (Nil Criticality)")
            print(" TODO #(2) See consequence of Outage and Cascading Failure data (With Criticality)")
            print("(3) Print system key data")
            print("(4) Graph output of whole system")
            print("(5) Sort nodes by highest Cyber reachability")
            print("# TODO (6) Compare CPS and CPSS Consequence Simulations")
            print("(B) Back ")
            queryData= input("Choose Option: ")
            print("You Selected " + queryData)
            
            if queryData == "1":
                menu_1_ConsequenceData()
            elif queryData == "2":
                menu_2_EMPTY()
            elif queryData == "3":
                menu_3_SystemKeyData()
            elif queryData == "4":
                menu_4_GraphGlobalNetwork()
            elif queryData == "5":
                menu_5_SortCyberReachability()
            elif queryData == "B" or queryData == "b":
                return 
            else:
                print("Error with setup option selected. Try again")

            print("----------------------------------------")

def menu_1_ConsequenceData():
    print("----------------------------------------")
    print("See Consequence of Outage and Cascading Failure Data with Nil Criticality Considerations")
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

    # Calculate consequences
    myNode = Globals.systemList[node]
    consequences = myNode.queryConsequences(number,0)

    # RECURSION IS BUGGY AND NOT WORKING STILL
    consequencePrint = []
    consequenceList = []
    for counter in consequences:
        consequencePrint.append(counter)
        currentLevel = consequences[counter]
        for pair in currentLevel:
            if pair:
                consequencePrint.append(pair.sysName)
                consequenceList.append(pair.sysName)


    print(f'Consequences of an outage at node {node} are: {consequencePrint}\n')

    
    # Now print the graph
    originalList = Globals.systemList
    sysNameList = []
    for counter in originalList:
        sysNameList.append(originalList[counter].sysName)

    graphList = []
    # Set all systems as False in beginning and set all seed values to false,
    # Unless is the original node (seed), or a consequence
    for system in sysNameList:
        isConsequence=False
        for consequence in consequenceList:
            if consequence in system:
                isConsequence=True
        if node == system:
           isSeed=True
        else:
            isSeed=False
        newGraphNode = CPSS_System.CPSS_forGraph(system,isSeed,isConsequence)
        graphList.append(newGraphNode)

    Graph.graphCascadingFailure(graphList)

    

# EMPTY
def menu_2_EMPTY():
    print("----------------------------------------")
    print("Text")
    print("----------------------------------------")
 

# See system jey data
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
    reachability = nodeObj.reachability

    affectorDict = nodeObj.affectorDict
    affectedByDict = nodeObj.affectedByDict

    finalAffector = []
    finalAffectedBy = []

    for affector, criticality in affectorDict:
        finalAffector.append(affector)
    
    for affectedBy, criticality in affectedByDict:
        finalAffectedBy.append(affectedBy)

    # Print output
    print(f'Key data for {node}\nCyber: {isCyber} | Physical: {isPhysical} | Social: {isSocial}')
    print(f'Node degree: {degree}')
    print(f'Node reachability: {reachability}')
    print(f'Systems that directly affect {node}:  {finalAffectedBy}.')
    print(f'Systems that {node} directly affects:  {finalAffector}.')
  
# See SubSystems within Larger Systems
def menu_4_GraphGlobalNetwork():
    print("----------------------------------------")
    print("Graph the Global Network of Systems")
    print("----------------------------------------")
    
    Graph.graphGlobalNetwork()
    print("done!")
  
def menu_5_SortCyberReachability():
    print("----------------------------------------")
    print("Sort and Print Nodes with Descending from Highest Cyber Reachability")
    print("----------------------------------------")
    
    valDict = {}

    for keyEntry in Globals.systemList:
        currentObj = Globals.systemList[keyEntry]
        if currentObj.isCyber:
            if currentObj.reachability in valDict:
                valDict[currentObj.reachability].append(currentObj.sysName)
            else:
                valDict[currentObj.reachability] = [currentObj.sysName]
    
    keys = list(valDict.keys())
    keys.sort(reverse=True)
    valDict_sort = {key: valDict[key] for key in keys}
        

    finalValDict = {}
  

    # Print output
    print(f'Cyber nodes with the highest reachability: {valDict_sort}\n')
    print("----------------------------------------")
  