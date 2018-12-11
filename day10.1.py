import matplotlib.pyplot as plt
import numpy as np
infile = open("day10.in", "r")
# infile = open("test.in", "r")
inString = infile.read()
inList = inString.splitlines()

# pointDict = {}
x_list = []
vx_list = []
y_list = []
vy_list = []

for line in inList:
    line = line.split('<')
    x = int(line[1].split(',')[0])
    y = int(line[1].split(',')[1].split('>')[0])
    vx = int(line[2].split(',')[0])
    vy = int(line[2].split(',')[1].strip('>'))
    x_list.append(x)
    y_list.append(y)
    vx_list.append(vx)
    vy_list.append(vy)
    # pointDict[(x,y)]={'x':x,'y':y,'vx':vx,'vy':vy,'t':0}

x_vec = np.array(x_list)
y_vec = np.array(y_list)
vx_vec = np.array(vx_list)
vy_vec = np.array(vy_list)

t = 0
tList = []
x_vec0 = x_vec
while True:
    t += 1
    x_vec0 = x_vec0 + vx_vec

    if len(np.unique(x_vec0)) < len(x_vec0)/3:
        print(np.unique(x_vec0))
        print(t)
        tList.append(t)
        if len(tList) > 10:
            break

def plotMessage(t,x_vec=x_vec,y_vec=y_vec,vx_vec=vx_vec,vy_vec=vy_vec):

    x_vec = x_vec + t*vx_vec
    y_vec = y_vec + t*vy_vec
    plt.scatter(x_vec,-y_vec)
    print(t)
    plt.show()

    return True

# for time in tList:
#     plotMessage(time)
plotMessage(10886)
