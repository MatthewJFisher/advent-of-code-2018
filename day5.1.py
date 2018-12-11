infile = open("day5.in", "r")
# infile = open("test.in", "r")
inString = infile.read()
inString = inString.strip()
inList = list(inString)

done = False
index = 1

while not done:
    if index > len(inList)-1:
        done = True
    elif inList[index]==inList[index-1].swapcase():
        del inList[index]
        del inList[index-1]
        index = index - 1

    else:
        index += 1

print(len(inList))
