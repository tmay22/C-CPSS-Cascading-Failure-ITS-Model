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
    # affectorList : list of all system objects that this system affects via consequence

    # Initialise object
    def __init__(self, inputName, inputCyber, inputPhysical, inputSocial):
        self.id = uuid4()
        self.sysName = inputName
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
        self.affectorList = []
        self.degree = 0
    
    # add an affector
    def addAffector(self, affector):
        self.affectorList.append(affector)
    
    def addDegree(self):
        self.degree = self.degree + 1

    # Add a Primary Input
    def addPrimaryInput(self, input):
        if input not in self.primaryInputs:
            self.primaryInputs.append(input)
            self.updatePrimary()
            # Add the affector to the input object
            input.addAffector(self)
            # Add a degree to src object
            input.addDegree()

    # Add a Primary Process
    def addPrimaryProcess(self, process):
        if process not in self.primaryProcesses:
            self.primaryProcesses.append(process)
            self.updatePrimary()
            # Add the affector to the process object
            process.addAffector(self)
            # Add a degree to src object
            process.addDegree()

    # Add a Primary Output
    def addPrimaryOutput(self, output):
        if output not in self.primaryOutputs:
            self.primaryOutputs.append(output)
            self.updatePrimary()
            # Add the affector to the output object
            output.addAffector(self)
            # Add a degree to src object
            output.addDegree()

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




    # Query what consequences failure of one node may have on the systems
    # Note does not remove duplicates
    def queryConsequences(self,  maximumOrderOfEffect, currentOrderOfEffect):
        # check to see if this has gone too far donw and stop infinite recursion
        if currentOrderOfEffect < maximumOrderOfEffect:
            # increase orderOfEffect
            currentOrderOfEffect = currentOrderOfEffect + 1
            currentLevelList = self.affectorList
            currentLevelDict = {}
            currentLevelDict[currentOrderOfEffect] = currentLevelList
            if currentLevelList:
                for item in currentLevelList:
                    itemEffects = item.queryConsequences(maximumOrderOfEffect, currentOrderOfEffect)
                    if itemEffects:
                        for key in itemEffects:
                            if key in currentLevelDict:
                                currentLevelDict[key].extend(itemEffects[key])
                            else:
                                currentLevelDict[key]=(itemEffects[key])
            return currentLevelDict
        else:
            return None        

