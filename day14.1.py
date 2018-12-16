import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter

infile = open("day13.in", "r")
# infile = open("test.in", "r")
inString = infile.read()
inList = inString.splitlines()

mapDict = {}
y = 0
cartIndex = 1
cartDict = {}
for line in inList:
    x = 0
    for char in line:
        if char == ' ' or char == '\n':
            x+=1
            continue
        elif char == 'v' or char == '^':
            mapDict[(x,y)] = {'type':'|','cart':cartIndex,'tick':0}
            if char == 'v':
                cartDict[cartIndex] = {'init':(x,y),'dir':(0,1),'pos':(x,y),'next':'L','tick':0}
            elif char == '^':
                cartDict[cartIndex] = {'init':(x,y),'dir':(0,-1),'pos':(x,y),'next':'L','tick':0}
            cartIndex +=1
        elif char == '<' or char == '>':
            mapDict[(x,y)] ={'type':'-','cart':cartIndex,'tick':0}
            if char == '<':
                cartDict[cartIndex] = {'init':(x,y),'dir':(-1,0),'pos':(x,y),'next':'L','tick':0}
            elif char == '>':
                cartDict[cartIndex] = {'init':(x,y),'dir':(1,0),'pos':(x,y),'next':'L','tick':0}
            cartIndex +=1
        else:
            mapDict[(x,y)] ={'type':char,'cart':False,'tick':0}
            # print(str((x,y))+' '+char)
        x+=1
    y+=1

first_collision = False
tick = 0
while not first_collision:
    cartList = cartDict.keys()
    cartList = sorted(cartList, key=lambda x: (cartDict[x]['pos'][1],cartDict[x]['pos'][0]))
    tick+=1
    for cart in cartList:
        old_pos = cartDict[cart]['pos']
        old_dir = cartDict[cart]['dir']
        old_next = cartDict[cart]['next']
        new_pos = (old_pos[0] + old_dir[0],old_pos[1] + old_dir[1])
        new_dir = old_dir
        new_next = old_next
        new_tick = tick
        mapDict[old_pos]['cart']=False
        # print('cart '+str(cart)+' moved to '+str(new_pos)+' on tick '+str(tick))
        if not mapDict[new_pos]['cart']:
            mapDict[new_pos]['cart']=cart
            if mapDict[new_pos]['type']=='/':
                if old_dir == (-1,0):
                    new_dir = (0,1)
                elif old_dir == (0,1):
                    new_dir = (-1,0)
                elif old_dir == (0,-1):
                    new_dir = (1,0)
                elif old_dir == (1,0):
                    new_dir = (0,-1)
                else:
                    print('Error - cart/map inconsistency')
                    print('cart '+str(cart)+' moved '+str(old_dir)+' into '+mapDict[new_pos]['type'])
            elif mapDict[new_pos]['type']=='\\':
                if old_dir == (1,0):
                    new_dir = (0,1)
                elif old_dir == (0,1):
                    new_dir = (1,0)
                elif old_dir == (0,-1):
                    new_dir = (-1,0)
                elif old_dir == (-1,0):
                    new_dir = (0,-1)
                else:
                    print('Error - cart/map inconsistency')
                    print('cart '+str(cart)+' moved '+str(old_dir)+' into '+mapDict[new_pos]['type'])
            elif mapDict[new_pos]['type']=='+':
                if old_next == 'L':
                    new_dir = (old_dir[1],-old_dir[0])
                    new_next = 'S'
                elif old_next == 'S':
                    new_next = 'R'
                elif old_next == 'R':
                    new_dir = (-old_dir[1],old_dir[0])
                    new_next = 'L'
            cartDict[cart]['pos'] = new_pos
            cartDict[cart]['dir'] = new_dir
            cartDict[cart]['next'] = new_next
            cartDict[cart]['tick'] = new_tick

        else:
            first_collision = True
            print(new_pos)
            break
