import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter

infile = open("day19.in", "r")
# infile = open("test.in", "r")
inString = infile.read()
inList = inString.splitlines()

reg = [1,0,0,0,0,0]

def addr(A,B,C,reg=reg):
    reg[C]=reg[A]+reg[B]
    return reg

def addi(A,B,C,reg=reg):
    reg[C]=reg[A]+B
    return reg

def mulr(A,B,C,reg=reg):
    reg[C]=reg[A]*reg[B]
    return reg

def muli(A,B,C,reg=reg):
    reg[C]=reg[A]*B
    return reg

def banr(A,B,C,reg=reg):
    reg[C]=reg[A] & reg[B]
    return reg

def bani(A,B,C,reg=reg):
    reg[C]=reg[A] & B
    return reg

def borr(A,B,C,reg=reg):
    reg[C]=reg[A] | reg[B]
    return reg

def bori(A,B,C,reg=reg):
    reg[C]=reg[A] | B
    return reg

def setr(A,B,C,reg=reg):
    reg[C]=reg[A]
    return reg

def seti(A,B,C,reg=reg):
    reg[C]=A
    return reg

def gtir(A,B,C,reg=reg):
    if A > reg[B]:
        reg[C] = 1
    else:
        reg[C] = 0
    return reg

def gtri(A,B,C,reg=reg):
    if reg[A] > B:
        reg[C] = 1
    else:
        reg[C] = 0
    return reg

def gtrr(A,B,C,reg=reg):
    if reg[A] > reg[B]:
        reg[C] = 1
    else:
        reg[C] = 0
    return reg

def eqir(A,B,C,reg=reg):
    if A == reg[B]:
        reg[C] = 1
    else:
        reg[C] = 0
    return reg

def eqri(A,B,C,reg=reg):
    if reg[A] == B:
        reg[C] = 1
    else:
        reg[C] = 0
    return reg

def eqrr(A,B,C,reg=reg):
    if reg[A] == reg[B]:
        reg[C] = 1
    else:
        reg[C] = 0
    return reg

line_num = 0
lineDict = {}

for line in inList:
    line = line.split(' ')
    if line[0][0]=='#':
        ip_reg = int(line[1])
    else:
        lineDict[line_num]=line[0]+'('+line[1]+','+line[2]+','+line[3]+')'
        line_num += 1
inst_pointer = reg[ip_reg]
count = 0
outfile = open("day19.out",'w+')
while(count < 1000):
    count +=1
    reg[ip_reg]=inst_pointer
    # print(lineDict[inst_pointer])
    eval(lineDict[inst_pointer])
    outfile.write(str(inst_pointer)+' '+str(reg)+'\n')
    print(inst_pointer,reg)
    inst_pointer = reg[ip_reg]+1
    if inst_pointer not in lineDict:
        break

print(reg[0])
