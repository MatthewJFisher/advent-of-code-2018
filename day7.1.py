from string import ascii_uppercase
# infile = open("day7.in", "r")
infile = open("/home/matthew/Downloads/input.txt", "r")
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

while len(stepDict) > len(stepList):
    allowedList = []
    for step in stepDict:
        allowed = True
        for step1 in stepDict[step]['after']:
            if step1 not in stepList:
                allowed = False
        if step in stepList or step in allowedList:
            allowed = False
        if allowed:
            allowedList.append(step)
    allowedList.sort()
    # print('allowed'+str(allowedList))
    stepList.append(allowedList[0])
    # print(stepList)
print(''.join(stepList))
