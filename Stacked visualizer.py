from classDefinitions import *
from graphics import *

import util
#This is the list of evens that are pruned in the data
EVENS = util.load("nevens.dat")
EVENSLIST= list(EVENS[1])

TEXT_SIZE = 12

#draws a given visTree in a window of a given width and height and a given border on the sides and top
def drawTree(tree, width, height, border):
    win = GraphWin(str(tree.n) + "x" + str(tree.m) +" tree", width, height)
    #Stores 2 lists of nodes and a node + position for later use drawing lines
    nodesList = []
    nodesPositionList = []
    #iterate through the nodes by their row and position in the row
    for row in range(tree.getHeight()):
        spacer = 1
        if len(tree.getLayers()[row])-1 !=0:
            #spaces the tree out so it is centered, avoiding a divide by 0
            spacer = len(tree.getLayers()[row])-1
        for node in range(len(tree.getLayers()[row])):
            #identify the point where the node goes
            pointTemp = Point(border + node * (width - 2 * border) / (spacer),
                              border + row * (height - border) / tree.getHeight())
            #define and draw the point
            textTemp = Text(pointTemp,
                            str(tree.getLayers()[row][node].getPath()[-1]))
            textTemp.setSize(TEXT_SIZE)
            textTemp.draw(win)
            #make it red if even
            if tuple(tree.getLayers()[row][node].getPath()) in EVENSLIST:
                textTemp.setFill("red")
            #update the list of nodes + positions for use when drawing lines
            nodesPositionList.append([tree.getLayers()[row][node], pointTemp])
            nodesList.append(tree.getLayers()[row][node])
    #Draws the lines
    for node in range(len(nodesList)):
        #if the node doesn't have a parent, there's nowehere to draw a line to
        if nodesList[node].parentNode == None:
            continue
        #get the position of the current node
        p1 = nodesPositionList[node][1]
        #Gets the position of the node's parent for this point
        p2 = nodesPositionList[nodesList.index(nodesList[node].parentNode)][1]
        lineTemp = Line(p1, p2)
        lineTemp.draw(win)
    

tree = visTree(5, 7)
treeLayers = tree.getLayers()
drawTree(tree, 1950, 1000, 100)

