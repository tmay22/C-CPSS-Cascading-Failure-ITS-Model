import Globals
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Graph that is temporarily made during setup IOT enable compute functions
def setupGraph():
    nodeList = Globals.systemList

    # Create blank directed graph canvas
    canvas = nx.DiGraph()
    # Add nodes
    for node in nodeList:
        canvas.add_node(node)
    # Add edges
    for node in nodeList:
        obj = nodeList[node]
        edgeList = obj.affectorDict
        firstNode = obj.sysName
        for affector in edgeList:
            secondNode, criticality = edgeList[affector]
            secondNode = secondNode
            canvas.add_edge(firstNode, secondNode, weight=criticality)
    # Lists i.e. Settings
    nodeSizes = [40] * len(canvas.nodes())  # Ensure nodeSizes matches the number of nodes
    color_map = ['blue'] * len(canvas.nodes())  # One color for each node
    edge_color = "grey"
    # Compute layout
    pos = nx.spring_layout(canvas)

    # Calculations
    nodes = list(canvas.nodes())
    totalNodes = len(nodes)

    # Calculate Reachability
    for eachNode in nodes:
        count = 0
        for secondNode in nodes:
            if nx.has_path(canvas,eachNode,secondNode):
                count = count + 1
        percentage = count/totalNodes
        currentObj = Globals.systemList[eachNode]
        currentObj.reachability = percentage


# Graph that is temporarily made during setup IOT enable compute functions
# Removes the system nodes that are purely social
def setupGraph_noSocial():
    nodeList = Globals.systemList

    # Create blank directed graph canvas
    canvas = nx.DiGraph()
    # Add nodes
    for node in nodeList:
        if nodeList[node].isCyber or nodeList[node].isPhysical:
            if not nodeList[node].isSocial:
                canvas.add_node(node)
    # Add edges
    for node in nodeList:
        if nodeList[node].isCyber or nodeList[node].isPhysical:
            if not nodeList[node].isSocial:
                obj = nodeList[node]
                edgeList = obj.affectorDict
                firstNode = obj.sysName
                for affector in edgeList:
                    if affector.isCyber or affector.isPhysical:
                        if affector.isSocial:
                            secondNode, criticality = edgeList[affector]
                            secondNode = secondNode
                            canvas.add_edge(firstNode, secondNode, weight=criticality)

    # Lists i.e. Settings
    nodeSizes = [40] * len(canvas.nodes())  # Ensure nodeSizes matches the number of nodes
    color_map = ['blue'] * len(canvas.nodes())  # One color for each node
    edge_color = "grey"
    # Compute layout
    pos = nx.spring_layout(canvas)

    # Calculations
    nodes = list(canvas.nodes())
    totalNodes = len(Globals.systemList)

    # Calculate Reachability
    for eachNode in nodes:
        count = 0
        for secondNode in nodes:
            if nx.has_path(canvas,eachNode,secondNode):
                count = count + 1
        percentage = count/totalNodes
        currentObj = Globals.systemList[eachNode]
        currentObj.noSocialReachability = percentage





# Show the global network of systems
def graphGlobalNetwork():
    nodeList = Globals.systemList

    # Create blank directed graph canvas
    canvas = nx.DiGraph()

    # Add nodes
    for node in nodeList:
        canvas.add_node(node)
    
    # Add edges
    for node in nodeList:
        obj = nodeList[node]
        edgeList = obj.affectorDict
        firstNode = obj.sysName
        for affector in edgeList:
            secondNode, criticality = edgeList[affector]
            secondNode = secondNode
            canvas.add_edge(firstNode, secondNode, weight=criticality)
    
    # Lists i.e. Settings
    nodeSizes = [40] * len(canvas.nodes())  # Ensure nodeSizes matches the number of nodes
    color_map = ['green'] * len(canvas.nodes())  # One color for each node
    edge_color = "grey"
    # Compute layout
    pos = nx.spring_layout(canvas)

    # Draw Canvas
    nx.draw(canvas, pos, with_labels=True, font_size=8, node_size=nodeSizes, 
            node_color=color_map, arrows=True, arrowsize=20, edge_color=edge_color)
    plt.show()



# Show the global network of systems

def graphCascadingFailure(nodeList):

    # Create blank directed graph canvas
    canvas = nx.DiGraph()
    # list to store colors for each node
    node_colours = []

    # Add nodes
    for node in nodeList:
        # ColourTest
        if node.isSeed:
            nodeColor="red"
        elif node.isConsequence:
            nodeColor="orange"
        else:
            nodeColor="green"
        canvas.add_node(node.sysName)
        node_colours.append(nodeColor)
    
    # Add edges
    for node in nodeList:
        obj = Globals.systemList[node.sysName]
        edgeList = obj.affectorDict
        firstNode = obj.sysName
        for affector in edgeList:
            secondNode, criticality = edgeList[affector]
            secondNode = secondNode
            canvas.add_edge(firstNode, secondNode, weight=criticality)
    
    # Lists i.e. Settings
    nodeSizes = [40] * len(nodeList)  # Ensure nodeSizes matches the number of nodes
    edge_color="grey"
    # Draw Canvas
    pos = nx.spring_layout(canvas)  # You can choose a different layout if needed
    nx.draw(canvas, pos, with_labels=True, font_size=8, node_size=nodeSizes, 
            node_color=node_colours, arrows=True, arrowsize=20, edge_color=edge_color)
    plt.show()

    