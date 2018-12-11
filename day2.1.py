infile = open("day2.in", "r")
inString = infile.read()
inList = inString.splitlines()

ct2 = 0
ct3 = 0

for item in inList:
    foundct2 = False
    foundct3 = False
    for char in item:

        if item.count(char) != 2 and item.count(char) !=3:
            continue
        if item.count(char) == 2 and not foundct2:
            foundct2 = True
        if item.count(char) == 3 and not foundct3:
            foundct3 = True

        if foundct2 and foundct3:
            ct2+=1
            ct3+=1
            break
    else:
        if foundct2:
            ct2 +=1
        if foundct3:
            ct3 +=1
print(ct2*ct3)
