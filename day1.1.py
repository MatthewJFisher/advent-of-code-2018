infile = open("day1.in", "r")
inString = infile.read()
inList = inString.splitlines()

freq = 0

for item in inList:
    sign = item[0]
    num = int(item[1:])
    if sign=='+':
        freq += num
    else:
        freq -= num
print(freq)
