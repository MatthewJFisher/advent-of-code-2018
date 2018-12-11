from string import ascii_uppercase
infile = open("day7.in", "r")
# infile = open("test.in", "r")
inString = infile.read()

inList = inString.splitlines()

stepDict = {}

for line in inList:
    step0 = line.split('tep ')[1][0]
    step1 = line.split('tep ')[2][0]
    if step0 not in stepDict:
        stepDict[step0] = {'before':[step1],'after':[]}
    else:
        stepDict[step0]['before'].append(step1)
    if step1 not in stepDict:
        stepDict[step1] = {'before':[],'after':[step0]}
    else:
        stepDict[step1]['after'].append(step0)

stepList = []

offset = -4
# offset = -64

workerDict = {}
numWorkers = 5

for i in range(numWorkers):
    workerDict[i] = {'step':'','time_left':0,'available':True}

time_elapsed = 0
waitList = []
while len(stepDict) > len(stepList):
    allowedList = []
    for step in stepDict:
        allowed = True
        for step1 in stepDict[step]['after']:
            if step1 not in stepList:
                allowed = False
        if step in stepList or step in allowedList or step in waitList:
            allowed = False
        if allowed:
            allowedList.append(step)
    allowedList.sort()
    for worker in workerDict:
        if workerDict[worker]['available'] and len(allowedList)>0:
            s = allowedList.pop(0)
            workerDict[worker]['step']=s
            waitList.append(s)
            workerDict[worker]['available']=False
            workerDict[worker]['time_left']=ord(s)+offset
    time_elapsed += 1
    for worker in workerDict:
        if not workerDict[worker]['available']:
            workerDict[worker]['time_left'] -= 1
            if workerDict[worker]['time_left'] == 0:
                workerDict[worker]['available'] = True
                stepList.append(workerDict[worker]['step'])
                waitList.remove(workerDict[worker]['step'])

print(time_elapsed)
