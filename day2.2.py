infile = open("day2.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inList = inString.splitlines()

nChar = len(inList[0])

for i in range(nChar):
    tempList = []
    for ID in inList:
        tempID = ID[0:i] + ID[i+1:]
        if tempID in tempList:
            print(tempID)
        tempList.append(tempID)
