import util
#This is the list of evens that are pruned in the data
EVENS = util.load("nevens.dat")
EVENSLIST= list(EVENS[1])

#This defines a class that represents 1 node in a visualizer tree
#With 2 fields, the value of the node, and whatever the parent node is
#if the node has no parent, then it's parentNode is None

class visNode:
    value = None
    parentNode = None

    #Constructor, creates a node that has a given value and parent node
    def __init__ (self, value, parent):
        self.value = value
        self.parentNode = parent

    #returns the path that leads to a node
    def getPath (self):
        if self.parentNode == None:
            return [self.value]
        parentPath = self.parentNode.getPath()
        parentPath.append(self.value)
        return parentPath

    #returns the number of layers deep that a node is in the tree
    def getHeight (self):
        if self.parentNode == None:
            return 1
        return 1 + self.parentNode.getLayer()

#This defines a tree that 
class visTree:
    nodes = []

    #Constructor: builds a tree with a given starting width to a given number of layers
    def __init__ (self, startingWidth, height):
        self.buildTree(startingWidth, height, None)

    #This is the actual function that builds the tree, it does so by creating a node with the given parent (previous)
    #adding it to the node list, and then creating every one of it's children until you reach the max height you want
    def buildTree (self, startingWidth, height, previous):
        if height == 0:
            return
        if previous != None and tuple(previous.getPath()) in EVENSLIST:
            return
        for i in reversed (range (1, startingWidth + 1)):
            temp = visNode(i, previous)
            self.nodes.append(temp)
            self.buildTree(i, height-1, temp)

