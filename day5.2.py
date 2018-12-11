from string import ascii_lowercase
from string import ascii_uppercase
infile = open("day5.in", "r")
# infile = open("test.in", "r")
inString = infile.read()
inString = inString.strip()
inList = list(inString)

minLength = len(inList)
print(minLength)
keyChar = ''

for char in ascii_lowercase:

    char_U = char.upper()
    tempString = inString
    print(char+char_U)
    if char in tempString:
        tempString = tempString.replace(char,'')
    if char_U in tempString:
        tempString = tempString.replace(char_U,'')

    tempList = list(tempString)
    done = False
    index = 1
    print(len(tempList))
    print(char in tempList)
    while not done:
        if index > len(tempList)-1:
            done = True
            if len(tempList) < minLength:
                minLength = len(tempList)
                print(minLength)
                keyChar = char
        elif tempList[index]==tempList[index-1].swapcase():
            del tempList[index]
            del tempList[index-1]
            index = index - 1

        else:
            index += 1
    print(len(tempList))
print(keyChar,minLength)
