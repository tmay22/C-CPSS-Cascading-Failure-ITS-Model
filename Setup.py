import CPSS_System
import Globals
import Graph
import csv

# Build System from a given path
def buildFromPath(path):

    # Set sub-paths for nodes and realtionships csvs
    nodePath = path+"SystemNodes.csv"
    nodeAffectors = path+"SystemAffectors.csv"

    # Create System Nodes
    with open(nodePath) as nodeFile:
        lineCount = 0
        csv_reader = csv.reader(nodeFile, delimiter=',')

        for row in csv_reader:
            # Set defaults
            name="default"
            cyber=False
            physical=False
            social=False

            # Get data from row if not title row
            if lineCount !=0:
                newName = row[0]
                newCyber = row[1]
                newPhysical = row[2]
                newSocial = row[3]

                # Check if name already exists
                if newName not in Globals.systemList:
                    name = newName
                    if newCyber == '1':
                        cyber= True
                    if newPhysical == '1':
                        physical = True
                    if newSocial == '1':
                        social = True
                    # Make Obj
                    sysObj = CPSS_System.systemNode(name,cyber,physical,social)
                    # Add to Globals
                    Globals.systemList[name] = sysObj      
            lineCount = lineCount+1
    # Cleanup

    del csv_reader
    del nodeFile

    # Create System Relationships

    with open(nodeAffectors) as relationFile:
        lineCount = 0
        csv_reader = csv.reader(relationFile, delimiter=',')

        for row in csv_reader:
            # set defaults
            sourceNode="default"
            destNode = "default"

            
            # Get data from row if not title row
            if lineCount !=0:
                sourceInput = row[0]
                destInput = row[1]
                criticalityInput = row[2]

                criticalityInput = int(criticalityInput)
                checkSrc = False
                checkDst = False
                # Check if name existts
                if sourceInput in Globals.systemList:
                    checkSrc = True
                if destInput in Globals.systemList:
                    checkDst = True

                # If both nodes exist create relationships
                if checkSrc and checkDst:
                    # Assign src and dest vals
                    sourceNode = sourceInput
                    destNode = destInput
                    
                    # Get Global Obj
                    dstObj = Globals.systemList[destNode]
                    srcObj = Globals.systemList[sourceNode]

                    srcObj.addAffector(dstObj, criticalityInput)
                    srcObj.addDegree()
                    dstObj.addAffectedBy(srcObj, criticalityInput)
                    
                    print("Conclusion")
            lineCount = lineCount + 1


    # Setup Graph

    Graph.setupGraph()

    

