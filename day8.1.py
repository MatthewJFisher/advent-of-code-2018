infile = open("day8.in", "r")
# infile = open("test.in", "r")
inString = infile.read()
inList = inString.split(' ')

inList = list(map(int, inList))

index = 0

def getNodeLen(inList, current_index):
    MDsum = 0
    nChildren = inList[current_index]
    nMD = inList[current_index+1]
    length = 2
    if nChildren > 0:
        for i in range(nChildren):
            index = current_index+length
            length += getNodeLen(inList, index)[0]
            MDsum +=getNodeLen(inList, index)[1]
    length += nMD

    for j in range(nMD):
        # print(MDsum)
        # print('length '+str(length))
        MDsum += inList[current_index+length-1-j]
    return(length, MDsum)



print(getNodeLen(inList,0))
