import csv
import matplotlib.pyplot as plt
import math as mt

def sum(r, n):
    s = 0
    for index in range(n):
        s += r
    return s

def approxA(i, n, y, x):
    a = ((sum(y, n) 
    * sum(mt.pow((1 / x), 2), n)) 
    - (sum((1 / x), n)
    * sum((y / x), n))) / ((n * sum(mt.pow((1 / x), 2), n))
    - (sum((1 / x), n)
    * sum((1 / x), n)))
    return a

def approxB(i, n, y, x):
    b = ((n * sum((y / x), n) 
    - (sum((1 / x), n) 
    * sum(y, n)))) / ((n * sum(mt.pow((1 / x), 2), n))
    - (sum((1 / x), n) 
    * sum((1 / x), n)))
    return b



file = open('2022_12_01_mcc.csv')
info = file.read().split('\n')
file.close()

for i in range(len(info)):
    info[i] = info[i].split(',')

for i in range(250834, len(info)):
    info.pop(i)

info.sort(key = lambda x: x[1])

for i in range(len(info)):
    info[i][1] = float(info[i][1])
    info[i][2] = float(info[i][2])

masX = []
masY = []
a = 0
b = 0

for i in range(len(info)):
    masX.append(info[i][2])
    a = approxA(i, len(info), info[i][1], info[i][2])
    b = approxB(i, len(info), info[i][1], info[i][2])
    masY.append(a + (b / info[i][2]))
    print((a + (b / info[i][2])), info[i][2])