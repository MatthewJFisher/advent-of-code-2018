infile = open("day3.in", "r")
# infile = open("test.in", "r")
inString = infile.read()
inList = inString.splitlines()

areaDict = {}
claimList = [i for i in range(1,len(inList)+1)]

for claim in inList:
    claim = claim.split('@')
    claimNum = int(claim[0].strip('#'))
    startX = int(claim[1].split(',')[0])
    startY = int(claim[1].split(',')[1].split(':')[0])
    lengthX = int(claim[1].split(',')[1].split(':')[1].split('x')[0])
    lengthY = int(claim[1].split('x')[1])
    for x in range(startX,startX+lengthX):
        for y in range(startY,startY+lengthY):
            if (x,y) not in areaDict:
                areaDict[(x,y)] = claimNum
            else:
                # areaDict[(x,y)].append(int(claim[0].strip('#')))
                if claimNum in claimList:
                    claimList.remove(claimNum)
                if areaDict[(x,y)] in claimList:
                    claimList.remove(areaDict[(x,y)])

print(claimList)
