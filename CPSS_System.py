import Globals

from uuid import uuid4

class CPSS_forGraph:
    
    # Object that is used for the graph generation
    # Sysname: system name
    # isSeed: true false for is the system is the source or seed of the failure
    # isConsequence: true false for if the system is a consequenec of the seed
    
    # Initialise object
    def __init__(self, sysName, isSeed, isConsequence):
        self.sysName = sysName
        self.isSeed = isSeed
        self.isConsequence = isConsequence

class ciaTriad:

    # Confidentiality, Availability, Integrity
    # Security class as per ARC-IT v 9.3

    def __init__(self, inputConfidentiality,  inputIntegrity, inputAvaliability, inputClass):
        self.confidentiality = inputConfidentiality
        self.integrity = inputIntegrity
        self.availability = inputAvaliability
        self.securityClass = inputClass

class systemNode:
    # A systemNode is a node that has inputs, processes and outputs
    # it can be a physical, social, cyber or "functional" node

    # Vars:
    # id: Identifier for object
    # name: name for the system
    # isCyber: boolean for if the system contains cyber components
    # isPhysical: boolean for if the system contains physical components
    # isSocial: boolean for if the system contains social components
    # affectorDict : list of all system objects that this system affects via consequence
    # affectedByDict : list of all the system objects that this system is effected by consequence
    # reachability : percentage of nodes in network that can be reached by this node
    # degree: amount of connections out
    # securityDict: security dictionary of serviceName and CIA triad score
    # arcgitectureLayer: WHat layer of the Arc-ITS architecture it is (e.g. Enterprise, physical, functional)


    # Initialise object #NEED TO INPUT ITS DATABASE TYPE
    def __init__(self, inputName, inputCyber, inputPhysical, inputSocial, inputArchitectureLayer):
        self.id = uuid4()
        tempName = f'[{inputArchitectureLayer}] {inputName}'
        self.sysName = tempName
        self.describeName = inputName
        self.isCyber = inputCyber
        self.isPhysical = inputPhysical
        self.isSocial = inputSocial
        self.affectorDict = {}
        self.affectedByDict = {}
        self.degree = 0
        self.reachability = 0
        self.securityDict = {}
        self.architectureLayer=inputArchitectureLayer


    
    # add an affector
    def addAffector(self, affectorName, criticality):
        self.affectorDict[affectorName] = affectorName.sysName, criticality
    
    # add an affected
    def addAffectedBy(self, affectedName, criticality):
        self.affectedByDict[affectedName] = affectedName.sysName, criticality
    
    # add a degree
    def addDegree(self):
        self.degree = self.degree + 1

    # Query what consequences failure of one node may have on the systems
    # Note does not remove duplicates
    def queryConsequences(self,  maximumOrderOfEffect, currentOrderOfEffect):
        # check to see if this has gone too far donw and stop infinite recursion
        if currentOrderOfEffect < maximumOrderOfEffect:
            # increase orderOfEffect
            currentOrderOfEffect = currentOrderOfEffect + 1
            currenntLevelAffectors = self.affectorDict
            currentLevelList = []
            for sysObj in currenntLevelAffectors:
                sysName, criticality = currenntLevelAffectors[sysObj]
                currentLevelList.append(sysObj)
            currentRecursionDict = {}
            currentRecursionDict[currentOrderOfEffect] = currentLevelList
            if currentLevelList:
                for item in currentLevelList:
                    itemEffects = item.queryConsequences(maximumOrderOfEffect, currentOrderOfEffect)
                    if itemEffects:
                        for key in itemEffects:
                            if key in currentRecursionDict:
                                currentRecursionDict[key].extend(itemEffects[key])
                            else:
                                currentRecursionDict[key]=(itemEffects[key])
            return currentRecursionDict
        else:
            breakpoint  

class informationFlow:
    # Object that describes the flow of information

    # flowName: name of the information flow
    # securityDict = dictionary of serviceName and CIA triad score
    # useFips = T/F FIPS standards

    def __init__(self, inputFlowName,):
        self.flowName = inputFlowName
        self.securityTriad = "empty"
        self.canAuthenticate = False
        self.useFips = False
        self.sourceDestList = []

class CPSS_forGraph:
    
    # Object that is used for the graph generation
    # Sysname: system name
    # isSeed: true false for is the system is the source or seed of the failure
    # isConsequence: true false for if the system is a consequenec of the seed
    
    # Initialise object
    def __init__(self, sysName, isSeed, isConsequence):
        self.sysName = sysName
        self.isSeed = isSeed
        self.isConsequence = isConsequence