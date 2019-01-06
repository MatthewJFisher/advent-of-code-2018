import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter

infile = open("day16.in", "r")
# infile = open("test.in", "r")
inString = infile.read()
inList = inString.splitlines()

funcDict = {}
funcDict_inv = {}
reg = [0,0,0,0]


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

func_list = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]

num = 0

for i in range(0,len(inList),4):

    if 'Before' in inList[i]:
        before = inList[i]
        inst = inList[i+1]
        after = inList[i+2]

        before = before.split(':')[1]
        before = before.strip().strip('[').strip(']').split(',')
        before = list(map(int,before))

        inst = list(map(int,inst.split(' ')))

        after = after.split(':')[1]
        after = after.strip().strip('[').strip(']').split(',')
        after = list(map(int,after))

        nFuncs = 0
        f = -1
        for i,func in enumerate(func_list):
            reg = before
            A,B,C = inst[1],inst[2],inst[3]
            if inst[0] not in funcDict:
                funcDict[inst[0]] = {'not':[]}
            if after != func(A,B,C,reg.copy()):
                if i not in funcDict[inst[0]]['not']:
                    funcDict[inst[0]]['not'].append(i)
            else:
                f = i
                nFuncs += 1
        if nFuncs ==1:
            funcDict[inst[0]]['is'] = f
            num += 1
    else:
        break

finalDict = {}
counter = 0
while len(finalDict)<16:
    for key in funcDict:
        if 'not' in funcDict[key] and 'is' not in funcDict[key]:
            if len(funcDict[key]['not'])==15:
                for i in range(16):
                    if i not in funcDict[key]['not']:
                        funcDict[key]['is'] = i
                        break
        if 'is' in funcDict[key]:
            tis = funcDict[key]['is']

            if key not in finalDict:
                finalDict[key] = tis
            for key1 in funcDict:
                if tis not in funcDict[key1]['not'] and key1 != key:
                    funcDict[key1]['not'].append(tis)
    # print(finalDict)
    # print(funcDict)

print(finalDict)

infile2 = open('day16.2.in','r')
inString2 = infile2.read()
inList2 = inString2.splitlines()

reg = [0,0,0,0]

for line in inList2:
    line = line.split(' ')
    inst = list(map(int,line))
    op = finalDict[inst[0]]
    A,B,C = inst[1],inst[2],inst[3]
    func = func_list[op]
    reg = func(A,B,C,reg)

print(reg)
