import Globals
from uuid import uuid4

class CPSS_System:
    # A system is a node that has inputs, processes and outputs

    # Vars:
    # id: Identifier for object
    # name: name for the system
    # isCyber: boolean for if the system contains cyber components
    # isPhysical: boolean for if the system contains physical components
    # isSocial: boolean for if the system contains social components
    # primaryInputs[]: list of other system objects that may act as inputs to this system
    # primaryProcesses[]: list of other system objects that may act as processes or sub-systems to this system
    # primaryOutputs[]: list of other system objects that may act as outputs to this system
    # primaryAll: list of all primary system objects
    # subInputs[]: list of the calculated inputs based on the subsystems contained within the object
    # subProcesses[]: list of the calculated processes based on the subsystems contained within the object
    # subOutputs[]: list of the calculated outputs based on the subsystems contained within the object
    # subAll: list of all sub system objects

    # Initialise object
    def __init__(self, inputName, inputCyber, inputPhysical, inputSocial):
        self.id = uuid4()
        self.name = inputName
        self.isCyber = inputCyber
        self.isPhysical = inputPhysical
        self.isSocial = inputSocial
        self.primaryInputs = []
        self.primaryProcesses = []
        self.primaryOutputs = []
        self.primaryAll = []
        self.subInputs = []
        self.subProcesses = []
        self.subOutputs = []
        self.subAll = []
    
    # Add a Primary Input
    def addPrimaryInput(self, input):
        self.primaryInputs.append(input)
        self.updatePrimary()

    # Add a Primary Process
    def addPrimaryProcess(self, process):
        self.primaryProcesses.append(process)
        self.updatePrimary()

    # Add a Primary Output
    def addPrimaryOutput(self, output):
        self.primaryOutputs.append(output)
        self.updatePrimary()

    # Updates all of the primary calculations
    def updatePrimary(self):
        self.primaryAll = self.primaryInputs + self.primaryProcesses + self.primaryOutputs
    # Updates the calculation for the sub functions
    def updateSub(self):
        self.subInputs = self.generateSubInputs(self, 1)
        self.subProcesses = self.generateSubProcesses(self, 1)
        self.subOutputs = self.generateSubOutputs(self, 1)
        self.subAll = self.subInputs + self.subProcesses + self.subOutputs
        
    # At current time, loopLevel is limited to 2
    #    
    def generateSubInputs(self, inputObj, loopLevel):
        # loopLevel stops the algorithm from endlessly recursing
        if loopLevel < 2:
            tempList = []
            if len(inputObj.primaryAll) > 0:
                for sys in inputObj.primaryAll:
                    tempInputs = sys.primaryInputs
                    if tempInputs != None:
                        tempList.extend(tempInputs)
                    tempInputs = inputObj.generateSubInputs(sys,2)
                    if tempInputs != None:
                        tempList.extend(tempInputs)
                return tempList
            else:
                return []



    def generateSubProcesses(self, inputObj, loopLevel):
        # loopLevel stops the algorithm from endlessly recursing
        if loopLevel < 2:
            tempList = []
            if len(inputObj.primaryAll) > 0:
                for sys in inputObj.primaryAll:
                    tempProcesses = sys.primaryProcesses
                    if tempProcesses != None:
                        tempList.extend(tempProcesses)
                    tempProcesses = inputObj.generateSubProcesses(sys,2)
                    if tempProcesses != None:
                        tempList.extend(tempProcesses)
                return tempList
            else:
                return []

 
    def generateSubOutputs(self, inputObj, loopLevel):
        if loopLevel < 2:
            tempList = []
            if len(inputObj.primaryAll) > 0:
                for sys in inputObj.primaryAll:
                    tempOutputs = sys.primaryOutputs
                    if tempOutputs != None:
                        tempList.extend(tempOutputs)
                    tempOutputs = inputObj.generateSubOutputs(sys,2)
                    if tempOutputs != None:
                        tempList.extend(tempOutputs)
                return tempList
            else:
                return []

        # loopLevel stops the algorithm from endlessly recursing           


if __name__ == '__main__':
    # Test
    # Create initial systems
    Chemist =  CPSS_System("Chemist", True, True, False)
    PharmacyStock = CPSS_System("PharmacyStock", False, True, False )
    Payments = CPSS_System("Payments", True, True, False)
    PharmacyService = CPSS_System("PharmacyService", True, True, True)
    Customers = CPSS_System("Customers", False, True, True)
    Orders = CPSS_System("Orders", True, True, False)
    Logistics = CPSS_System("Logistics", False, True, False)
    Delivery = CPSS_System("Delivery", False, True, True)
    CreditCards = CPSS_System("CreditCards", True, True, False)
    FundsTransfer = CPSS_System("FundsTransfer", True, True, False)
    PrintReceipt = CPSS_System("PrintReceipt", True, True, False)
    Pharmacists = CPSS_System("Pharmacists", False, True, True)
    Dispensary = CPSS_System("Dispensary", False, True, False)
    ScriptProcessing = CPSS_System("ScriptProcessing", True, True, False)
    # Consolidate into single list
    systemList = [Chemist, PharmacyStock, Payments, PharmacyService, Customers, Orders, Logistics, Delivery, 
                  CreditCards, FundsTransfer, PrintReceipt, Pharmacists, Dispensary, ScriptProcessing]
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
    PharmacyService.addPrimaryOutput(Dispensary)
    # Update all
    for sys in systemList:
        sys.updateSub()
    print("here")