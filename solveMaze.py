# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 08:17:23 2023

@author: Charles
"""
maze=[
    '*******',
    '* *   *',
    '*o*x  *',
    '*     *',
    '*******'
]

#move directions
north = (0, -1)
south = (0, 1)
east = (1, 0)
west = (-1, 0)

#mapping of turns
turnLeft = {north:east, east:south, south:west, west:north}
turnRight = {north:west, west:south, south:east, east:north}
turnBack = {north:south, west:east, south:north, east:west}

#start direction
moveDirection = south
currentPosition = [-1, -1]

#display current maze state
def showMaze():
    for r in theMaze:
        print(''.join(r))
#return character in maze at the test position    
def testPosition(direction):
    global theMaze
    global currentPosition
    return theMaze[currentPosition[0] + direction[0]][currentPosition[1] + direction[1]]

#try out the moves and update the current direction
def doMove():
    global moveDirection
    testDirection = turnRight[moveDirection]
    te = testPosition(testDirection)
    if te != '*':
        moveDirection = testDirection
        return te
    else:
        te = testPosition(moveDirection)
        if te != '*':
            return te
    testDirection = turnLeft[moveDirection]
    te = testPosition(testDirection)
    if te != '*':
        moveDirection = testDirection
        return te
    testDirection = turnBack[moveDirection]
    te = testPosition(testDirection)
    if te != '*':
        moveDirection = testDirection
        return te
    #no possible move
    return 'z'
    

startPosition = [-1, -1]
endPosition = [-1, -1]

row = -1
theMaze = []
#unpack maze into 2d array of characters. Detect start and end
for m in maze:
    row += 1
    colStart = m.find('o')
    colEnd = m.find('x')
    if  colStart > -1:
        startPosition = [row, colStart]
    if  colEnd > -1:
        endPosition = [row, colEnd]
    theMaze.append(list(m))
#showMaze()

if  endPosition[0] == -1:
    print('Maze end not found')
else:    
    if  startPosition[0] > -1:
        currentPosition = startPosition[:]
        print(tuple(currentPosition));
        #loop until no valid move
        while True:
            isStart = currentPosition == startPosition
            theMaze[currentPosition[0]][currentPosition[1]] = 'v'
            nextChar = doMove()
            currentPosition[0] += moveDirection[0]
            currentPosition[1] += moveDirection[1]
            #showMaze()
            if nextChar == 'z':
                print('No possible move.')
                break
            if nextChar == 'x':
                print(tuple(currentPosition));
                print(' Got there!')
                break
            if isStart and nextChar == 'v':
                print('Exit is unreachable')
                break
            print(tuple(currentPosition));
            
    else:
        #start position was not defined
        print('Maze start not found')

        
        
        
    