import CPSS_System
import Globals
import Graph
import csv

# Build System from a given path
def buildFromPath(path):

    # Set sub-paths for nodes and realtionships csvs
    nodePath = path+"Node_Names.csv"
    nodeSecurity = path + "Node_Security.csv"
    nodeFlows = path+"Flow_SourceDest.csv"
    flowSecurity = path + "Flow_Security.csv"
    flowComms = path + "Flow_Comms.csv"


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
                newLayer = row[4]


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
                    sysObj = CPSS_System.systemNode(name,cyber,physical,social,newLayer)
                    newArchName = f'[{newLayer}] {name}'
                    # Add to Globals
                    Globals.systemList[newArchName] = sysObj      
            lineCount = lineCount+1
    # Cleanup

    del csv_reader
    del nodeFile

    # Physical security assignment

    with open(nodeSecurity) as nodeSecurityFile:
        lineCount = 0
        csv_reader = csv.reader(nodeSecurityFile, delimiter=',')

        for row in csv_reader:
            # Set defaults
            nodeName = "unknown"
            securityClass = "unknown"
            confidentiality = "unknown"
            integrity = "unknown"
            availability = "unknown"
            servicePackage = "unknown"

            # Get data from row if not title row
            if lineCount !=0:
                newNodeName = row[0]
                newSecurityClass = row[1]
                newConfidentiality = row[2]
                newIntegrity = row[3]
                newAvailability = row[4]
                newServicePackage = row[5]
                newArchitecture = row[6]

                name = f'[{newArchitecture}] {newNodeName}'

                # Check if name exists, add to object's security dict
                if name in Globals.systemList:
                    currentSystemObj = Globals.systemList[name]
                    currentDict = currentSystemObj.securityDict
                    newCIA = CPSS_System.ciaTriad(newConfidentiality, newIntegrity, newAvailability, newSecurityClass)      
                    currentDict[newServicePackage]=newCIA
            lineCount = lineCount+1
    # Cleanup

    del csv_reader
    del nodeSecurityFile



    # Create System Relationships

    with open(nodeFlows) as relationFile:
        lineCount = 0
        csv_reader = csv.reader(relationFile, delimiter=',')

        for row in csv_reader:
            # set defaults
            sourceNode="default"
            infoFlow = "default"
            destNode = "default"

            
            # Get data from row if not title row
            if lineCount !=0:
                sourceInput = row[0]
                flowInput = row[1]
                destInput = row[2]
                sourceType = row[3]
                destType = row[4]

                sourceName = f'[{sourceType}] {sourceInput}'
                destName = f'[{destType}] {destInput}'
                checkSrc = False
                checkDst = False
                # Check if name existts
                if sourceName in Globals.systemList:
                    checkSrc = True
                if destName in Globals.systemList:
                    checkDst = True

                # If both nodes exist create relationships
                if checkSrc and checkDst:
                    # Assign src and dest vals
                    sourceNode = sourceName
                    destNode = destName
                    
                    # Get Global Obj
                    dstObj = Globals.systemList[destNode]
                    srcObj = Globals.systemList[sourceNode]

                    srcObj.addAffector(dstObj, 100)
                    srcObj.addDegree()
                    dstObj.addAffectedBy(srcObj, 100)
                    
                    # Create new information flow in Globals as long as it isn't a relationship
                    if 'relationship' not in flowInput:
                        if flowInput in Globals.informationFlowList:
                            activeFlow = Globals.informationFlowList[flowInput]
                            sourceDest = srcObj, dstObj
                            activeFlow.sourceDestList.append(sourceDest)
                        else:
                            activeFlow = CPSS_System.informationFlow(flowInput)
                            sourceDest = srcObj, dstObj
                            activeFlow.sourceDestList.append(sourceDest)
                            Globals.informationFlowList[flowInput] = activeFlow
                    


                   
                    
            lineCount = lineCount + 1

    del csv_reader
    del relationFile



    # Create Flow Security

    with open(flowSecurity) as flowSecurityFile:
        lineCount = 0
        csv_reader = csv.reader(flowSecurityFile, delimiter=',')

        for row in csv_reader:
            # set defaults
            infoFlow = "default"
            confidentiality = "unknown"
            integrity = "unknown"
            availability = "unknown"
            fips = False

            
            # Get data from row if not title row
            if lineCount !=0:
                flowInput = row[0]
                confidentialityInput = row[1]
                integrityInput = row[2]
                availabilityInput = row[3]
                fipsInput = row[4]

                checkSrc = False
                # Check if name existts
                if flowInput in Globals.informationFlowList:
                    checkSrc = True

                # If flow exists
                if checkSrc :
                    # Set booleans
                    if "TRUE" in fipsInput:
                        fipsInput = True
                    else:
                        fipsInput = False
                    
                    cia = CPSS_System.ciaTriad(confidentialityInput,integrityInput, availabilityInput, "unassigned")
                    flowObj = Globals.informationFlowList[flowInput]
                    flowObj.securityTriad = cia
                    flowObj.useFips = fipsInput
            
            lineCount = lineCount + 1

    del csv_reader
    del flowSecurityFile

    # Create Flow Communications Data Layer

    with open(flowComms) as flowCommsFile:
        lineCount = 0
        csv_reader = csv.reader(flowCommsFile, delimiter=',')

        for row in csv_reader:
          
            # Get data from row if not title row
            if lineCount !=0:
                profileName = row[0]
                levelName = row[1]
                informationFlow = row[2]

                checkSrc = False
                # Check if name existts
                if informationFlow in Globals.informationFlowList:
                    checkSrc = True

                # check if commProfile exists
                if profileName in Globals.communicationProfiles:
                    checkComm = True
                else:
                    checkComm = False

                
                # If flow exists
                if checkSrc:
                    inforFlowObj = Globals.informationFlowList[informationFlow]
                    if not checkComm:
                        newProfile = CPSS_System.communicationProfiles(profileName)
                        inforFlowObj.addDict(levelName, profileName)
                        newProfile.linkedFlows.append(inforFlowObj)
                        inforFlowObj.commProfiles.append(newProfile)
                        Globals.communicationProfiles[profileName]=newProfile
                    else:
                        getProfile = Globals.communicationProfiles[profileName]
                        inforFlowObj.addDict(levelName, profileName)
                        getProfile.linkedFlows.append(inforFlowObj)
                        inforFlowObj.commProfiles.append(getProfile)
            
            lineCount = lineCount + 1

    # Add flow instance of degree statistics
    for counter in Globals.communicationProfiles:
        profile = Globals.communicationProfiles[counter]
        linkedFlowList = profile.linkedFlows
        totalLinks = 0
        for linkedFlow in linkedFlowList:
            numRelies = len(linkedFlow.sourceDestList)
            totalLinks = totalLinks + numRelies
        profile.instanceOfDegree = totalLinks

    # Setup Graph

    Graph.setupGraph()
    Graph.setupGraph_noSocial()

    

