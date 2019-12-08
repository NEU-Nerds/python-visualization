import util
#This is the list of evens that are pruned in the data
# EVENS = util.load("nevens.dat")
# EVENSLIST= list(EVENS[1])
EVENSLIST = util.loadOldEvens("4x31.json")

#This defines a class that represents 1 node in a visualizer tree
#With 3 fields, the value of the node, whatever the parent node is, and if the node is even
#if the node has no parent, then it's parentNode is None

class visNode:
    value = None
    parentNode = None
    isEven = None

    #Constructor, creates a node that has a given value and parent node
    def __init__ (self, value, parent):
        self.value = value
        self.parentNode = parent
        if tuple(self.getPath()) in EVENSLIST:
            self.isEven = True
        else:
            self.isEven = False
        
    #returns the path that leads to a node as a list
    def getPath (self):
        if self.parentNode == None:
            return [self.value]
        parentPath = self.parentNode.getPath()
        parentPath.append(self.value)
        return parentPath

    #returns the number of layers deep that a node is in the tree as an int
    def getHeight (self):
        if self.parentNode == None:
            return 1
        return 1 + self.parentNode.getHeight()

    #returns a numerical representation of the node (really only used for sorting the tree of nodes)
    def __getNumberRep__ (self):
        rep = 10*self.getHeight()
        pathTemp = self.getPath()
        for x in range(self.getHeight()):
            rep+=pathTemp[x]/(10**x)
        return rep

#This defines a tree that
class visTree:
    m = 0
    n = 0
    nodes = []

    #Constructor: builds a tree with a given starting width to a given number of layers sorted vertically and horizontally
    def __init__ (self, startingWidth, height):
        self.n = startingWidth
        self.m = height
        self.buildTree(startingWidth, height, None)
        self.nodes.sort(key=lambda node: node.__getNumberRep__())

    #This is the actual function that builds the tree, it does so by creating a node with the given parent (previous)
    #adding it to the node list, and then creating every one of it's children until you reach the max height you want
    def buildTree (self, startingWidth, height, previous):
        if height == 0:
            return
        if previous != None and previous.isEven:
            return
        for i in reversed (range (1, startingWidth + 1)):
            temp = visNode(i, previous)
            self.nodes.append(temp)
            self.buildTree(i, height-1, temp)

    #this is a function that returns the height of the tree (number of layers) as an int
    def getHeight (self):
        h = 0
        for node in self.nodes:
            if node.getHeight() > h:
                h=node.getHeight()
        return h


    #This returns a list representing the list nodes at each
    #height in order (so the 0th index is row 1, 1st index row 2 etc.)
    def getLayers(self):
        layers = [[] for i in range(self.getHeight())]
        for node in self.nodes:
            layers[node.getHeight()-1].append(node)
        return layers
