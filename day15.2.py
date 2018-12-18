import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
from collections import deque

infile = open("day15.in", "r")
# infile = open("test.in", "r")
inString = infile.read()
inList = inString.splitlines()
size = len(inList)
charDict = {}
mapDict = {}

cIndex = 1
nG = 0
nE = 0
elf_attack_power = 3
goblin_attack_power = 3

y = 0

for line in inList:
    x = 0
    line = line.strip()
    for char in line:
        if char == 'G' or char == 'E':
            if char == 'G':
                nG +=1
            elif char == 'E':
                nE +=1
            charDict[cIndex] = {'type':char,'pos':(x,y),'hp':200}
            mapDict[(x,y)] = {'type':'.','occupied':cIndex,'open':False}
            cIndex += 1
        elif char == '.':
            mapDict[(x,y)] = {'type':char,'occupied':False,'open':True}

        elif char == '#':
            mapDict[(x,y)] = {'type':char,'occupied':False,'open':False}
        x+=1
    y+=1

nE0 = nE
nG0 = nG

directions = [(0,-1),(-1,0),(1,0),(0,1)]

def getDistance(pos0,pos1,mapDict=mapDict):
    openSet = set()
    for node in mapDict:
        if mapDict[node]['open']:
            openSet.add(node)
    # openNodes[pos0] = 0
    openDeque = deque()
    openDeque.append((pos0,0))
    while len(openDeque)>0:
        pos0tup = openDeque.popleft()
        pos0 = pos0tup[0]
        if pos0 == pos1:
            return(pos0tup[1])
        for dir in directions:
            pos = (pos0[0]+dir[0],pos0[1]+dir[1])
            if pos in openSet:
                openDeque.append((pos,1 + pos0tup[1]))
                openSet.discard(pos)

def findTarget(char0,charList,charDict=charDict,mapDict=mapDict):
    distList = []
    pos0 = charDict[char0]['pos']
    if charDict[char0]['type'] == 'G':
        for char1 in charList:
            if char1 not in charDict:
                continue
            if charDict[char1]['type'] == 'E':
                for dir in directions:
                    pos = (charDict[char1]['pos'][0]+dir[0],charDict[char1]['pos'][1]+dir[1])
                    if pos == charDict[char0]['pos']:
                        distList.append((0,pos[0],pos[1]))
                    if mapDict[pos]['open']:
                        # print('Getting distance')
                        dist = getDistance(pos0,pos)
                        if not dist:
                            continue
                        # print(dist)
                        distList.append((dist,pos[0],pos[1]))

    elif charDict[char0]['type'] == 'E':
        for char1 in charList:
            if char1 not in charDict:
                continue
            if charDict[char1]['type'] == 'G':
                for dir in directions:
                    pos = (charDict[char1]['pos'][0]+dir[0],charDict[char1]['pos'][1]+dir[1])
                    if pos == charDict[char0]['pos']:
                        distList.append((0,pos[0],pos[1]))
                    if mapDict[pos]['open']:
                        # print(pos0,pos)
                        # print('Getting distance')
                        dist = getDistance(pos0,pos)
                        if not dist:
                            continue
                        # print(dist)
                        distList.append((dist,pos[0],pos[1]))
    distList = sorted(distList, key=itemgetter(0,2,1))
    if not distList:
        return(False)
    if distList[0][0] == 10000:
        return(False)
    target = (distList[0][1],distList[0][2])

    return(target)

def showMap(mapDict,charDict):

    for j in range(size):
        lineString = ''
        for i in range(size):
            char = mapDict[(i,j)]['occupied']
            if not char:
                lineString+=mapDict[(i,j)]['type']
            else:
                lineString+=charDict[char]['type']
        print(lineString)


def getMove(char0,target,charDict=charDict,mapDict=mapDict):
    candList = []
    pos = charDict[char0]['pos']
    if pos == target:
        return(pos)
    for dir in directions:
        candidate = (pos[0]+dir[0],pos[1]+dir[1])
        if mapDict[candidate]['open']:
            dist = getDistance(target,candidate)
            # if char0 == 1:
            #     print(target,candidate,dist)
            if dist is not None:
                candList.append((dist,candidate[0],candidate[1]))

    candList = sorted(candList, key=itemgetter(0,2,1))
    # print(pos)
    # print(target)
    # print(candList)
    if not candList:
        # print('error during the move of ' + str(char0))
        return(False)
    move = (candList[0][1],candList[0][2])

    return(move)

def attack(char0,charDict=charDict,mapDict=mapDict):
    pos = charDict[char0]['pos']
    enemies = []
    for dir in directions:
        candidate = (pos[0]+dir[0],pos[1]+dir[1])
        if not mapDict[candidate]['occupied']:
            continue
        elif charDict[char0]['type'] == charDict[mapDict[candidate]['occupied']]['type']:
            continue
        else:
            enemyID = mapDict[candidate]['occupied']
            enemyHP = charDict[enemyID]['hp']
            enemies.append((enemyHP,candidate[1],candidate[0],enemyID))

    enemies = sorted(enemies, key=itemgetter(0,1,2))
    enemyID = enemies[0][3]
    enemyPos = (enemies[0][2],enemies[0][1])
    if charDict[char0]['type']=='E':
        attack_power = elf_attack_power
    else:
        attack_power = goblin_attack_power
    charDict[enemyID]['hp'] -= attack_power
    if charDict[enemyID]['hp'] < 1:
        mapDict[enemyPos]['occupied'] = False
        mapDict[enemyPos]['open'] = True
        enemyType = charDict[enemyID]['type']
        del charDict[enemyID]
        return(enemyType)
    else:
        return(False)

def makeMove(char0,move,charDict=charDict,mapDict=mapDict):
    pos0 = charDict[char0]['pos']
    mapDict[pos0]['occupied'] = False
    mapDict[pos0]['open'] = True
    charDict[char0]['pos'] = move
    mapDict[move]['occupied'] = char0
    mapDict[move]['open'] = False

for i in range(1):
    elf_attack_power = 16
    done = False
    doneEarly = False

    nRounds = 0
    while not done:
        if nRounds % 1 == 0:
            print('working on round ' + str(nRounds))
            showMap(mapDict,charDict)
        charList = charDict.keys()
        charList = sorted(charList, key=lambda x: (charDict[x]['pos'][1],charDict[x]['pos'][0]))
        for char0 in charList:
            if char0 not in charDict:
                continue
            # print('Beginning of turn for character ' + str(char0))

            if nG == 0 or nE == 0:
                doneEarly = True
                break
            pos0 = charDict[char0]['pos']
            # print('Finding target')
            target = findTarget(char0,charList,charDict,mapDict)
            if not target:
                continue
            # print('Getting move')
            move = getMove(char0,target)
            if not move:
                continue
            if move == pos0:
                # print('Attacking')
                killed = attack(char0)
                if killed == 'G':
                    nG -= 1
                elif killed == 'E':
                    nE -= 1
                    done=True
            else:
                # print('Making move')
                makeMove(char0,move)
                if move == target:
                    # print('Attacking (2)')
                    killed = attack(char0)
                    if killed == 'G':
                        nG -= 1
                    elif killed == 'E':
                        nE -= 1

        if doneEarly:
            break
        if nE == 0 or nG == 0:
            done = True
        nRounds += 1
        showMap(mapDict,charDict)


HPsum = 0
for char in charDict:
    HPsum += charDict[char]['hp']
print(str(nE0-nE)+' elves died')
print(nRounds)
print(HPsum)
print(nRounds*HPsum)
# print(getDistance((1,2),(1,5)))
