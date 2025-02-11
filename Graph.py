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
        edgeList = obj.affectorList
        firstNode = obj.sysName
        for affector in edgeList:
            secondNode = affector.sysName
            canvas.add_edge(firstNode, secondNode)
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
        edgeList = obj.affectorList
        firstNode = obj.sysName
        for affector in edgeList:
            secondNode = affector.sysName
            canvas.add_edge(firstNode, secondNode)
    
    # Lists i.e. Settings
    nodeSizes = [40] * len(canvas.nodes())  # Ensure nodeSizes matches the number of nodes
    color_map = ['blue'] * len(canvas.nodes())  # One color for each node
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
            nodeColor="green"
        else:
            nodeColor="blue"
        canvas.add_node(node.sysName)
        node_colours.append(nodeColor)
    
    # Add edges
    for node in nodeList:
        obj = Globals.systemList[node.sysName]
        edgeList = obj.affectorList
        firstNode = obj.sysName
        for affector in edgeList:
            secondNode = affector.sysName
            canvas.add_edge(firstNode, secondNode)
    
    # Lists i.e. Settings
    nodeSizes = [40] * len(nodeList)  # Ensure nodeSizes matches the number of nodes
    edge_color="grey"
    # Draw Canvas
    pos = nx.spring_layout(canvas)  # You can choose a different layout if needed
    nx.draw(canvas, pos, with_labels=True, font_size=8, node_size=nodeSizes, 
            node_color=node_colours, arrows=True, arrowsize=20, edge_color=edge_color)
    plt.show()

    