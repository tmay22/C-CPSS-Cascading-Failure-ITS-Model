import CPSS_System
import Globals
import Graph

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
