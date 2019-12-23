from classDefinitions import *
from graphics import *
import util

class batchWin:
    width = None
    height = None
    border = None
    batch = None
    window = None

    #Number, Number, Ordered Set -> batchWin
    #this is a function that creates and begins visualizing an iterateable 
    #collection of boardStates (visNodes or ordered groupings of numbers) provided
    def __init__(self, width, height, border, batch):
        self.width = width
        self.height = height
        self.border = border
        self.batch = batch
        self.window = GraphWin("Batch Visualizer", width, height)
        self.drawBoard()

    #draws the board at the position in the batch it is in
    def drawBoard(self):
        position = 0
        while(True):
            clearRect = Rectangle(Point(0,0), Point(self.width, self.height))
            clearRect.setFill("white")
            clearRect.setOutline("white")
            clearRect.draw(self.window)
            if isinstance(self.batch[position], visNode):
                boardState = self.batch[position].getPath()
            else:
                boardState = self.batch[position]
            SQUARE_WIDTH = ((self.width - 2 * self.border) / boardState[0])
            SQUARE_HEIGHT = ((self.height - 2 * self.border) / len(boardState))
            for row in range(len(boardState)):
                for col in range(boardState[row]):
                    pointOne = Point(self.border + col * SQUARE_WIDTH,
                                     self.border + row * SQUARE_HEIGHT)
                    pointTwo = Point(self.border + (col + 1) * SQUARE_WIDTH,
                                     self.border + (row + 1) * SQUARE_HEIGHT)
                    rectTemp = Rectangle(pointOne, pointTwo)
                    rectTemp.draw(self.window)
            keyString = self.window.getKey()
            if keyString == "Left":
                position -= 1
            elif keyString == "Right":
                position += 1
            if position == -1:
                position = (len(self.batch) - 1)
            if position == len(self.batch):
                position = 0

#This stuff down here is just to visualize the evens. It's specific to my path
#so it's gonna break when I push it


EVENSLIST = []
for x in range(1,16):
    EVENSLIST.append(util.load("../../../Desktop/evens/evens" + str(x) + ".dat"))

flat_evens = []
for sublist in EVENSLIST:
    for item in sublist:
        flat_evens.append(item)


b1 = batchWin(1000, 1000, 25, flat_evens)
