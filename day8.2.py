infile = open("day8.in", "r")
# infile = open("test.in", "r")
inString = infile.read()
inList = inString.split(' ')

inList = list(map(int, inList))

index = 0

def getNodeLen(inList, current_index):
    MDsum = 0
    value = 0
    nChildren = inList[current_index]
    nMD = inList[current_index+1]
    length = 2
    if nChildren > 0:
        valueList = []
        for i in range(nChildren):
            index = current_index+length
            length += getNodeLen(inList, index)[0]
            valueList.append(getNodeLen(inList, index)[1])
    length += nMD
    if nChildren == 0:
        for j in range(nMD):

            value += inList[current_index+length-1-j]
    if nChildren > 0:
        for j in range(nMD):
            print(inList[current_index+length-1-j])
            print(valueList)
            if inList[current_index+length-1-j]-1 < len(valueList):
                value += valueList[inList[current_index+length-1-j]-1]
    return(length, value)


print(getNodeLen(inList,0))
