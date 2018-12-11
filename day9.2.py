from collections import deque
# players = 9
# lastMarble = 25

# players = 17
# lastMarble = 1104

players = 410
lastMarble = 7205900

marbleList = [0]
marbleDeque = deque()
marbleDeque.append(0)

scoreDict = {}
for i in range(players):
    scoreDict[i] = 0

currentIndex = 0
marbleNum = 0

def takeTurn(playerNum,marbleNum,currentIndex=currentIndex,marbleDeque=marbleDeque):
    score = 0
    length = len(marbleDeque)
    if marbleNum % 23 != 0:
        # currentIndex += 2
        marbleDeque.rotate(-2)
        marbleDeque.appendleft(marbleNum)

    else:
        score = marbleNum
        marbleDeque.rotate(7)
        score += marbleDeque.popleft()

    return(score, currentIndex)

currentPlayer = 0

while(marbleNum < lastMarble):
    marbleNum += 1
    if marbleNum%100000==0:
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
