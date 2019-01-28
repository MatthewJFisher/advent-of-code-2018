import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter

infile = open("day18.in", "r")
# infile = open("test.in", "r")
inString = infile.read()
inList = inString.splitlines()

xrange = len(inList[0])
yrange = len(inList)

stateDict = {}

#setup initial state
for y,line in enumerate(inList):
    for x,char in enumerate(line):
        if char == '.':
            stateDict[(x,y)]={'state':'O','nO':0,'nL':0,'nT':0}
        elif char == '#':
            stateDict[(x,y)]={'state':'L','nO':0,'nL':0,'nT':0}
        elif char == '|':
            stateDict[(x,y)]={'state':'T','nO':0,'nL':0,'nT':0}
        else:
            print('Bad character!')

#update neighbor counts
def updateNeighborCount(stateDict=stateDict,xrange=xrange,yrange=yrange):

    for x in range(xrange):
        for y in range(yrange):
            nO,nL,nT = 0,0,0
            for nx in range(x-1,x+2):
                for ny in range(y-1,y+2):
                    if (nx,ny)==(x,y):
                        continue
                    elif (nx,ny) not in stateDict:
                        continue
                    if stateDict[(nx,ny)]['state']=='O':
                        nO+=1
                    if stateDict[(nx,ny)]['state']=='L':
                        nL+=1
                    if stateDict[(nx,ny)]['state']=='T':
                        nT+=1
            stateDict[(x,y)]['nO']=nO
            stateDict[(x,y)]['nL']=nL
            stateDict[(x,y)]['nT']=nT

def nextState(stateDict=stateDict,xrange=xrange,yrange=yrange):
    for x in range(xrange):
        for y in range(yrange):
            newstate = ''
            if stateDict[(x,y)]['state']=='O':
                if stateDict[(x,y)]['nT']>2:
                    newstate = 'T'
                else:
                    newstate = 'O'
            elif stateDict[(x,y)]['state']=='T':
                if stateDict[(x,y)]['nL']>2:
                    newstate = 'L'
                else:
                    newstate = 'T'
            elif stateDict[(x,y)]['state']=='L':
                if stateDict[(x,y)]['nL']>0 and stateDict[(x,y)]['nT']>0:
                    newstate = 'L'
                else:
                    newstate = 'O'
            stateDict[(x,y)]['state']=newstate
    updateNeighborCount()

def getResult(stateDict=stateDict,xrange=xrange,yrange=yrange):
    countT = 0
    countL = 0
    for x in range(xrange):
        for y in range(yrange):
            if stateDict[(x,y)]['state']=='L':
                countL += 1
            elif stateDict[(x,y)]['state']=='T':
                countT += 1
    return countT*countL

updateNeighborCount()
for i in range(10):
    nextState()

print(getResult())
