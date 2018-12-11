from datetime import datetime as dt
from datetime import timedelta as td
infile = open("day4.in", "r")
# infile = open("test.in", "r")
inString = infile.read()
inList = inString.splitlines()


nightDict = {}

for line in inList:
    date = line.split(']')[0].strip('[')
    time = date.split(' ')[1]
    d = dt.strptime(date,'%Y-%m-%d %H:%M')
    minute = d.minute
    hour = d.hour
    if hour < 1:
        d = d - td(days=1) # associating the hour past midnight with the previous day

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
        for minute in range(asleep_time[nap],awake_time[nap]):
            guardDict[guard][minute]+=1
            guardDict[guard]['TotalSleep']+=1

maxSleep = 0
sleepyGuard = ''

for guard in guardDict:
    if guardDict[guard]['TotalSleep']>maxSleep:
        maxSleep = guardDict[guard]['TotalSleep']
        sleepyGuard = guard



# print(guardDict[sleepyGuard])
maxSleepMinute = 0
bestMinute = -1

for minute in guardDict[sleepyGuard]:
    if str(minute).isalpha():
        continue
    if guardDict[sleepyGuard][minute] > maxSleepMinute:
        maxSleepMinute = guardDict[sleepyGuard][minute]
        bestMinute = minute


print(bestMinute*sleepyGuard)
