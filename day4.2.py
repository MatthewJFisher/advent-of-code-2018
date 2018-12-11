from datetime import datetime as dt
from datetime import timedelta as td
infile = open("day4.in", "r")
# infile = open("test.in", "r")
inString = infile.read()
inList = inString.splitlines()

# monthDict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

nightDict = {}

for line in inList:
    date = line.split(']')[0].strip('[')
    time = date.split(' ')[1]
    d = dt.strptime(date,'%Y-%m-%d %H:%M')
    # minute = int(time.split(':')[1])
    # hour = int(time.split(':')[0])
    # month = int(date.split('-')[1])
    # day = int(date.split('-')[2])

    minute = d.minute
    hour = d.hour
    if hour < 1:
        d = d - td(days=1)

    day = d.day
    month = d.month
    event = line.split(']')[1]

    if (month,day) not in nightDict:
        nightDict[(month,day)]=['X',[],[]]
    if 'Guard' in event:
        guardNum = int(event.split('#')[1].split()[0])
        nightDict[(month,day)][0]=guardNum

    elif 'falls' in event:
        nightDict[(month,day)][1].append(minute)
    elif 'wakes' in event:
        nightDict[(month,day)][2].append(minute)

guardDict = {}

for night in nightDict:
    if nightDict[night][0] == 'X':
        print('Error, no Guard found for '+str(night))
        break
    data = nightDict[night]
    # print(data)
    guard = data[0]
    if guard not in guardDict:
        guardDict[guard]={}
        for i in range(60):
            guardDict[guard][i]=0
            guardDict[guard]['TotalSleep']=0
    asleep_time = data[1]
    awake_time = data[2]
    asleep_time.sort()
    awake_time.sort()
    if len(asleep_time)!=len(awake_time):
        print("Error, time mismatch")
    for nap in range(len(asleep_time)):
        # print(asleep_time, awake_time)
        for minute in range(asleep_time[nap],awake_time[nap]):
            guardDict[guard][minute]+=1
            guardDict[guard]['TotalSleep']+=1

maxSleep = 0
bestMin = -1
sleepyGuard = ''

for guard in guardDict:
    for minute in range(60):
        if guardDict[guard][minute]>maxSleep:
            maxSleep = guardDict[guard][minute]
            sleepyGuard = guard
            bestMin = minute

print(bestMin*sleepyGuard)
