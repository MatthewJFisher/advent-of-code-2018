import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter

infile = open("day16.in", "r")
# infile = open("test.in", "r")
inString = infile.read()
inList = inString.splitlines()

sampleDict = {}
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
        for func in func_list:
            reg = before
            A,B,C = inst[1],inst[2],inst[3]
            # print('Before = ' + str(before))
            # print(str(func(A,B,C,reg.copy())))
            # print('After = ' + str(after))
            if after == func(A,B,C,reg.copy()):
                nFuncs += 1
            # print('\n')

        if nFuncs > 2:
            num += 1


    else:
        break

print(num)
