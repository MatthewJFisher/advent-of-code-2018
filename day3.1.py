infile = open("day3.in", "r")
# infile = open("test.in", "r")
inString = infile.read()
inList = inString.splitlines()

areaDict = {}

X = 1000
Y = 1000

for claim in inList:
    claim = claim.split('@')
    startX = int(claim[1].split(',')[0])
    startY = int(claim[1].split(',')[1].split(':')[0])
    lengthX = int(claim[1].split(',')[1].split(':')[1].split('x')[0])
    lengthY = int(claim[1].split('x')[1])
    for x in range(startX,startX+lengthX):
        for y in range(startY,startY+lengthY):
            if (x,y) not in areaDict:
                areaDict[(x,y)] = 1
            else:
                areaDict[(x,y)] += 1

overlaps = 0

for i in range(X):
    for j in range(Y):
        if (i,j) in areaDict:
            if areaDict[(i,j)] > 1:
                overlaps += 1

print(overlaps)
