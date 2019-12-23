from classDefinitions import *
from graphics import *

import util
#draws a given boardState (either a node or a list of numbers) in
#a window of given width, height and give border on all 4 sides
def drawBoard(inputState, width, height, border):
    win = GraphWin("board", width, height)
    if isinstance(inputState, visNode):
        boardState = inputState.getPath()
    else:
        boardState = inputState
    SQUARE_HEIGHT = ((width - 2 * border) / boardState[0])
    SQUARE_WIDTH = ((height - 2 * border) / len(boardState))
    for row in range(len(boardState)):
        for col in range(boardState[row]):
            pointOne = Point(border + col * SQUARE_HEIGHT,
                             border + row * SQUARE_WIDTH)
            pointTwo = Point(border + (col + 1) * SQUARE_HEIGHT,
                             border + (row + 1) * SQUARE_WIDTH)
            rectTemp = Rectangle(pointOne, pointTwo)
            rectTemp.draw(win)


drawBoard([5, 3, 3, 2, 2, 1], 1000, 1000 , 25)
