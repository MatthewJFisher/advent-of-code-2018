infile = open("day6.in", "r")
# infile = open("test.in", "r")
inString = infile.read()

inList = inString.splitlines()

xMin = 0
xMax = 0
yMin = 0
yMax = 0

nodeDict = {}

for node in inList:
    x = int(node.split(',')[0])
    y = int(node.split(',')[1])
    nodeDict[(x,y)] = [False]
    if x < xMin:
        xMin = x
    if x > xMax:
        xMax = x
    if y < yMin:
        yMin = y
    if y > yMax:
        yMax = y

def findClosestNode(X,Y, nodeDict=nodeDict, xMin=xMin, xMax=xMax, yMin=yMin, yMax=yMax):
    min = xMax-xMin+yMax-yMin
    closeNode = []
    for node in nodeDict:
        distance = abs(node[0]-X)+abs(node[1]-Y)

        if distance < min:
            min = distance
            closeNode = [node]
        elif distance == min:
            closeNode.append(node)
    return(closeNode)

for i in range(xMin,xMax+1):
    for j in range(yMin,yMax+1):
        edge = False

        closeNodes = findClosestNode(i,j)
        if len(closeNodes) > 1:
            continue
        if (i == xMin or i == xMax or j == yMin or j == yMax):
            edge = True
        for node in closeNodes:
            nodeDict[node].append((i,j))
            if not nodeDict[node][0] and edge:
                nodeDict[node][0]=edge
maxArea = 0

for node in nodeDict:
    if nodeDict[node][0]:
        continue
    area = len(nodeDict[node])-1
    if area > maxArea:
        maxArea = area

# print(nodeDict)

print(maxArea)
