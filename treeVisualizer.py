from graphics import *
import math
import util

win = GraphWin("Chomp Tree", 1000, 1000)
LL = 100
R=5
EVENS = util.load("nevens.dat")
EVENSLIST= list(EVENS[1])

#This draws a tree for an m by n board at the given position x, y on the given window across a given angle (in raidans)
def drawTree(win, m, n, x, y, startAngle, endAngle, previous):
    deltaAngle= endAngle-startAngle
    if n>0:
        temp4 = Text (Point(x+10, y+10), util.listToString(previous))
        temp4.setFill("black")
        temp4.draw(win)
    if tuple(previous) in EVENSLIST and n>0:
        temp = Circle(Point(x,y), R)
        temp.setFill("red")
        temp.draw(win)
        return
    if n==0:
        return
    temp = Circle(Point(x,y), R)
    temp.setFill("green")
    temp.draw(win)
    
    for i in range (1, m+1):
        if m==1:
            sc=0
        else:
            sc=1/(m-1)
        temp3 = previous[:]
        temp3.append(i)
        #print(temp3)
        if n > 1:
            temp2 = Line(Point(x,y), Point(x+LL*math.cos(startAngle+(i-1)*sc*deltaAngle),
                                       y+LL*math.sin(startAngle+(i-1)*sc*deltaAngle)))
            temp2.draw(win)
        
        drawTree(win, i, n-1, x+LL*math.cos(startAngle+(i-1)*sc*deltaAngle),
                 y+LL*math.sin(startAngle+(i-1)*sc*deltaAngle),
                 startAngle+(i-1)*deltaAngle/m, startAngle+i*deltaAngle/m, temp3)
    
    
        
        



drawTree(win, 5, 5, 500, 500, 0, 31/16*math.pi, [])

"""
    Line(Point(x, y), Point(x+LL*math.cos(angle),y+LL*math.sin(angle))).draw(win)
    Circle(Point(x,y), 10).draw(win)
    drawTree(win, m, n-1, x+LL*math.cos(angle),y+LL*math.sin(angle), angle)
"""
