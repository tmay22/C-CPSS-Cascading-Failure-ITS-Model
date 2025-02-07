import Globals
import networkx as nx
import matplotlib.pyplot as plt

# Show the global network of systems
def graphGlobalNetwork():
    nodeList = Globals.systemList

    # Create blank graph canvas
    canvas = nx.Graph()

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
    nodeSizes = [20]
    color_map = ['blue']

    # Draw Canvas
    nx.draw(canvas, with_labels=True, font_size=14, node_size=nodeSizes, node_color=color_map)
    plt.show()



# Show the global network of systems
def graphCascadingFailure(nodeList):

    # Create blank graph canvas
    canvas = nx.Graph()

    # Add nodes
    for node in nodeList:
        # ColourTest
        if node.isSeed:
            color="red"
        elif node.isConsequence:
            color="green"
        else:
            color="blue"
        canvas.add_node(node, {"color":color})
    
    # Add edges
    for node in nodeList:
        obj = nodeList[node]
        edgeList = obj.affectorList
        firstNode = obj.sysName
        for affector in edgeList:
            secondNode = affector.sysName
            canvas.add_edge(firstNode, secondNode)
    
    # Lists i.e. Settings
    nodeSizes = [20]
    
    # Draw Canvas
    nx.draw(canvas, with_labels=True, font_size=14, node_size=nodeSizes)
    plt.show()

