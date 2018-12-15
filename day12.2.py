import matplotlib.pyplot as plt
import numpy as np
infile = open("day12.in", "r")
# infile = open("test.in", "r")
inString = infile.read()
inList = inString.splitlines()

stateDict = {}
ruleDict = {}

for line in inList:
    if line == '':
        continue
    if line[0] == 'i':
        state = line.split(':')[1].strip().replace('#','1').replace('.','0')
        stateDict[0]=(0,state)

    if line[0]=='.' or line[0]=='#':
        rule = line.split('=>')[0].strip().replace('.','0').replace('#','1')
        result = line.split('=>')[1].strip().replace('#','1').replace('.','0')
        ruleDict[rule] = result

numGen = 10000

for i in range(numGen):
    potID0 = stateDict[i][0]
    state = stateDict[i][1]
    length0 = len(state)
    state = state.lstrip('0')
    lZerosRemoved = length0-len(state)
    state = state.rstrip('0')
    state = '00000'+state+'00000'
    potID0 = potID0 + lZerosRemoved - 5
    index = 0
    temp_state = '00'
    while index + 5 < len(state):

        group = ''
        for j in range(index,index+5):
            group += state[j]

        if group in ruleDict:
            temp_state += ruleDict[group]
        else:
            temp_state += '0'
        index += 1
    stateDict[i+1]=(potID0,temp_state)

ID = stateDict[numGen][0]+50000000000-numGen
sum = 0

print(stateDict[numGen])

for pot in stateDict[numGen][1]:
    plant = int(pot)
    sum += plant*ID
    ID += 1

print(sum)
