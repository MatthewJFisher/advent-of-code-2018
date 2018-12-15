import matplotlib.pyplot as plt
import numpy as np

# serial = 42 # test
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

sumDict = {}
sumTable = {}


for x in range(1,xMax+1):
    for y in range(1,yMax+1):
        power = getCellPower(x,y)
        # sumDict[(x,y,1)]=power
        if x > 1:
            power += sumTable[(x-1,y)]
        if y > 1:
            power += sumTable[(x,y-1)]
        if x > 1 and y > 1:
            power -= sumTable[(x-1,y-1)]
        sumTable[(x,y)]=power

for s in range(1,301):
    for x in range(1,xMax+2-s):
    # print('working on column '+str(x))
        for y in range(1,yMax+2-s):

            powerSum=sumTable[(x+s-1,y+s-1)]
            if x > 1:
                powerSum-=sumTable[(x-1,y+s-1)]
            if y > 1:
                powerSum-=sumTable[(x+s-1,y-1)]
            if x > 1 and y > 1:
                powerSum+=sumTable[(x-1,y-1)]

            sumDict[(x,y,s)]=powerSum

maxPower = 0
maxPowerCell = ()

for cell in sumDict:
    if sumDict[cell] > maxPower:
        maxPower = sumDict[cell]
        maxPowerCell = cell

print(str(maxPowerCell).strip('(').strip(')').replace(' ',''))
