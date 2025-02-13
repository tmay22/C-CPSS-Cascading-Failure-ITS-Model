import CPSS_System
import Globals
import Graph
import csv

def defaultBuild():

    # Test
    # Create initial systems
    Chemist =  CPSS_System.CPSS_System("Chemist", True, True, False)
    PharmacyStock = CPSS_System.CPSS_System("PharmacyStock", False, True, False )
    Payments = CPSS_System.CPSS_System("Payments", True, True, False)
    PharmacyService = CPSS_System.CPSS_System("PharmacyService", True, True, True)
    Customers = CPSS_System.CPSS_System("Customers", False, True, True)
    Orders = CPSS_System.CPSS_System("Orders", True, True, False)
    Logistics = CPSS_System.CPSS_System("Logistics", False, True, False)
    Delivery = CPSS_System.CPSS_System("Delivery", False, True, True)
    CreditCards = CPSS_System.CPSS_System("CreditCards", True, True, False)
    FundsTransfer = CPSS_System.CPSS_System("FundsTransfer", True, True, False)
    PrintReceipt = CPSS_System.CPSS_System("PrintReceipt", True, True, False)
    Pharmacists = CPSS_System.CPSS_System("Pharmacists", False, True, True)
    Dispensary = CPSS_System.CPSS_System("Dispensary", False, True, False)
    ScriptProcessing = CPSS_System.CPSS_System("ScriptProcessing", True, True, False)
    # Consolidate into single list
    Globals.systemList["Chemist"] = Chemist
    Globals.systemList["PharmacyStock"] = PharmacyStock
    Globals.systemList["Payments"] = Payments
    Globals.systemList["PharmacyService"] = PharmacyService
    Globals.systemList["Customers"] = Customers
    Globals.systemList["Orders"] = Orders
    Globals.systemList["Logistics"] = Logistics
    Globals.systemList["Delivery"] = Delivery
    Globals.systemList["CreditCards"] = CreditCards
    Globals.systemList["FundsTransfer"] = FundsTransfer
    Globals.systemList["PrintReceipt"] = PrintReceipt
    Globals.systemList["Pharmacists"] = Pharmacists
    Globals.systemList["Dispensary"] = Dispensary
    Globals.systemList["ScriptProcessing"] = ScriptProcessing
    # Add inputs, processes, and outputs to each node
    # Chemist
    Chemist.addPrimaryInput(PharmacyStock)
    Chemist.addPrimaryProcess(Payments)
    Chemist.addPrimaryProcess(PharmacyService)
    Chemist.addPrimaryOutput(Customers)
    # PharmecuticalStock
    PharmacyStock.addPrimaryInput(Orders)
    PharmacyStock.addPrimaryProcess(Logistics)
    PharmacyStock.addPrimaryOutput(Delivery)
    # Payments
    Payments.addPrimaryInput(CreditCards)
    Payments.addPrimaryProcess(FundsTransfer)
    Payments.addPrimaryOutput(PrintReceipt)
    # PharmacyService
    PharmacyService.addPrimaryInput(Pharmacists)
    PharmacyService.addPrimaryProcess(ScriptProcessing)
    PharmacyService.addPrimaryProcess(PharmacyStock)
    PharmacyService.addPrimaryOutput(Dispensary)
    # Update all
    for sys in Globals.systemList.values():
        sys.updateSub()

    Graph.setupGraph()


# Build System from a given path
def buildFromPath(path):

    # Set sub-paths for nodes and realtionships csvs
    nodePath = path+"SystemNodes.csv"
    nodeRelationships = path+"SystemRelationships.csv"

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
                    sysObj = CPSS_System.CPSS_System(name,cyber,physical,social)
                    # Add to Globals
                    Globals.systemList[name] = sysObj      
            lineCount = lineCount+1
    # Cleanup

    del csv_reader
    del nodeFile

    # Create System Relationships

    with open(nodeRelationships) as relationFile:
        lineCount = 0
        csv_reader = csv.reader(relationFile, delimiter=',')

        for row in csv_reader:
            # set defaults
            sourceNode="default"
            ipo = "unknown"
            destNode = "default"
            
            # Get data from row if not title row
            if lineCount !=0:
                sourceInput = row[0]
                ipoInput = row[1]
                destInput = row[2]

                # Determine if Input, Process or Output
                if "Input" in ipoInput:
                    ipo = "Input"
                elif "Process" in ipoInput:
                    ipo = "Process"
                elif "Output" in ipoInput:
                    ipo = "Output"

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
                    if "Input" in ipo:
                        dstObj.addPrimaryInput(srcObj)
                    elif "Process" in ipo:
                        dstObj.addPrimaryProcess(srcObj)
                    elif "Output" in ipo:
                        dstObj.addPrimaryOutput(srcObj)
                    dstObj.updateSub()
                    # Update all
                    for sys in Globals.systemList.values():
                        sys.updateSub()
                    print("Conclusion")
            lineCount = lineCount + 1

    # Update all
    for sys in Globals.systemList.values():
        sys.updateSub()
    

    # Setup Graph

    Graph.setupGraph()

    

