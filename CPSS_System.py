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
    # noSocialReachability : percentage of all nodes in network that can be reached by this node if exclusive social nodes are removed (of origianl node count)

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
        self.noSocialReachability = 0
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

    # Query what consequences failure of one node may have on the systems
    # Note does not remove duplicates
    # Does not consider nodes that are only social
    def queryConsequences_noSocial(self,  maximumOrderOfEffect, currentOrderOfEffect):
        # check to see if this has gone too far donw and stop infinite recursion
        if currentOrderOfEffect < maximumOrderOfEffect:
            # increase orderOfEffect
            currentOrderOfEffect = currentOrderOfEffect + 1
            currenntLevelAffectors = self.affectorDict
            currentLevelList = []
            for sysObj in currenntLevelAffectors:
                sysName, criticality = currenntLevelAffectors[sysObj]
                if sysObj.isCyber or sysObj.isPhysical:
                    if not sysObj.isSocial:
                        currentLevelList.append(sysObj)
            currentRecursionDict = {}
            currentRecursionDict[currentOrderOfEffect] = currentLevelList
            if currentLevelList:
                for item in currentLevelList:
                    itemEffects = item.queryConsequences_noSocial(maximumOrderOfEffect, currentOrderOfEffect)
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
    # commProfiles = Data layer of Communications solutions
    # communicationsDictionary: levels are 1-ItsApplicationEntity , 2-Facilities, 3-Security, 4-Management, 5-TransNet, 6-Access, 7-Unspecified
    

    def __init__(self, inputFlowName,):
        self.flowName = inputFlowName
        self.id = uuid4()
        self.securityTriad = "empty"
        self.canAuthenticate = False
        self.useFips = False
        self.sourceDestList = []
        self.commProfiles= []
        self.communicationsDictionary = {}
        self.communicationsDictionary["1-ItsApplicationEntity"]=[]
        self.communicationsDictionary["2-Facilities"]=[]
        self.communicationsDictionary["3-Security"]=[]
        self.communicationsDictionary["4-Management"]=[]
        self.communicationsDictionary["5-TransNet"]=[]
        self.communicationsDictionary["6-Access"]=[]
        self.communicationsDictionary["7-Unspecified"]=[]
        # Add an entry to the communications dictionary
    def addDict(self, levelName, commsProfile):
        if "ITS Application Entity" in levelName:
            dictSearch = "1-ItsApplicationEntity"
        elif "Facilities" in levelName:
            dictSearch = "2-Facilities"
        elif "Security" in levelName:
            dictSearch = "3-Security"
        elif "Mgmt" in levelName:
            dictSearch = "4-Management"
        elif "TransNet" in levelName:
            dictSearch = "5-TransNet"
        elif "Access" in levelName:
            dictSearch = "6-Access"
        else:
            dictSearch = "7-Unspecified"
        
        arrayVal = self.communicationsDictionary[dictSearch]
        arrayVal.append(commsProfile)
        
class communicationProfiles:
    # Object that represents a communication solution

    # solutionId: identifier of solution
    # solutionName: name of the communication solution
    # linkedFLows = linked informationFLows
    def __init__(self, inProfileName):
        self.profileName = inProfileName
        self.id = uuid4()

        self.linkedFlows = []
        

    

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