import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter

infile = open("day16.in", "r")
# infile = open("test.in", "r")
inString = infile.read()
inList = inString.splitlines()

tileDict = {}
y_min = 1000
y_max = 0
for line in inList:
    line = line.split(',')
    tempDict = {}
    for entry in line:
        entry = entry.split('=')
        xy = entry[0]
        vals = entry[1]
        if '..' in vals:
            vals = list(map(int,vals.split('..')))
        else:
            vals = [int(vals)]
        tempDict[xy] = vals
    for x in range(tempDict['x'][0],tempDict['x'][-1]+1):
        for y in range(tempDict['y'][0],tempDict['y'][-1]+1)
            if y < y_min:
                y_min = y
            if y > y_max:
                y_max = y
            tileDict[(x,y)] = '\#'

nodeList = []
usedList = []
stillWaterList = []
def trackWater(source,y_max,y_min,tileDict=tileDict, nodeList=nodeList, usedList=usedList):
    x = source[0]
    y = source[1]
    if (x,y+1) in tileDict:
