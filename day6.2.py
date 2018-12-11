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

def findTotalDistance(X,Y, nodeDict=nodeDict):

    totalDistance = 0
    for node in nodeDict:
        totalDistance += abs(node[0]-X)+abs(node[1]-Y)

    return(totalDistance)

safeArea = 0

for i in range(xMin-200,xMax+201):
    for j in range(yMin-200,yMax+201):

        distance = findTotalDistance(i,j)
        if distance < 10000:
            safeArea+=1


print(safeArea)
