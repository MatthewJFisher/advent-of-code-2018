import matplotlib.pyplot as plt
import numpy as np

# serial = 57 # test
serial = 7672

xMax = 300
yMax = 300

def getCellPower(x,y, serial=serial):
    rID = x + 10
    level = rID * y
    level += serial
    level = level * rID
    # print(str(level))
    if len(str(level)) < 3:
        level = 0
    else:
        level = int(str(level)[-3])
    level -= 5
    return(level)

cellDict = {}

for x in range(1,xMax+1):
    for y in range(1,yMax+1):
        cellDict[(x,y)]=getCellPower(x,y)

sumDict = {}

for x in range(1,xMax-1):
    for y in range(1,yMax-1):
        powerSum = 0
        for i in range(x,x+3):
            for j in range(y,y+3):
                powerSum+=cellDict[(i,j)]
        sumDict[(x,y)]=powerSum

maxPower = 0
maxPowerCell = ()

for cell in sumDict:
    if sumDict[cell] > maxPower:
        maxPower = sumDict[cell]
        maxPowerCell = cell

print(maxPower,maxPowerCell)
