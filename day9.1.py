# players = 9
# lastMarble = 25

# players = 17
# lastMarble = 1104

players = 410
lastMarble = 72059

marbleList = [0]

scoreDict = {}
for i in range(players):
    scoreDict[i] = 0

currentIndex = 0
marbleNum = 0

def takeTurn(playerNum,marbleNum,currentIndex=currentIndex,marbleList=marbleList):
    score = 0
    if marbleNum % 23 != 0:
        currentIndex += 2
        while currentIndex > len(marbleList):
            currentIndex -= len(marbleList)
        if currentIndex==len(marbleList):
            marbleList.append(marbleNum)
        else:
            marbleList.insert(currentIndex,marbleNum)
    else:
        score = marbleNum
        currentIndex -= 7
        while currentIndex < 0:
            currentIndex += len(marbleList)
        if currentIndex == len(marbleList) - 1:
            score += marbleList.pop(currentIndex)
            currentIndex = 0
        else:
            score += marbleList.pop(currentIndex)


    return(score, currentIndex)

currentPlayer = 0

while(marbleNum < lastMarble):
    marbleNum += 1
    if marbleNum%10000==0:
        print('working on #'+str(marbleNum))
    currentScore,currentIndex = takeTurn(currentPlayer,marbleNum,currentIndex)
    scoreDict[currentPlayer] += currentScore
    currentPlayer += 1
    if currentPlayer == players:
        currentPlayer = 0

highScore = 0

for player in scoreDict:
    if scoreDict[player]>highScore:
        highScore = scoreDict[player]

print(highScore)
