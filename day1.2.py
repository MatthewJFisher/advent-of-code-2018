infile = open("day1.in", "r")
# infile = open("test.in", "r")

inString = infile.read()
inList = inString.splitlines()

freq = 0

freqList = []

found = False

while not found:
    print("Length of list: " + str(len(freqList)))
    for item in inList:
        if freq in freqList:
            found = True
            print(freq)
            break
        else:
            freqList.append(freq)

        sign = item[0]
        num = int(item[1:])
        if sign=='+':
            freq += num
        else:
            freq -= num
