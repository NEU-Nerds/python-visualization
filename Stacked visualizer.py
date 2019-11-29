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
    nodesList = []
    nodesPositionList = []
    for row in range(tree.getHeight()):
        spacer = 1
        if len(tree.getLayers()[row])-1 !=0:
            spacer = len(tree.getLayers()[row])-1
        for node in range(len(tree.getLayers()[row])):
            pointTemp = Point(border + node * (width - 2 * border) / (spacer),
                              border + row * (height - border) / tree.getHeight())
            textTemp = Text(pointTemp,
                            str(tree.getLayers()[row][node].getPath()[-1]))
            textTemp.setSize(TEXT_SIZE)
            textTemp.draw(win)
            if tuple(tree.getLayers()[row][node].getPath()) in EVENSLIST:
                textTemp.setFill("red")
            nodesPositionList.append([tree.getLayers()[row][node], pointTemp])
            nodesList.append(tree.getLayers()[row][node])
    for node in range(len(nodesList)):
        if nodesList[node].parentNode == None:
            continue
        p1 = nodesPositionList[node][1]
        p2 = nodesPositionList[nodesList.index(nodesList[node].parentNode)][1]
        lineTemp = Line(p1, p2)
        lineTemp.draw(win)
    

tree = visTree(5, 7)
treeLayers = tree.getLayers()
drawTree(tree, 1950, 1000, 100)

