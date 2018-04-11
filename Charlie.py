#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:40:25 2017

@author: Seyed
"""
from random import randint
from itertools import combinations
import math

def solution(cost,starting_tokens):
    p = cost
    n = starting_tokens
    tosses = 20
    x = []
    
    for i in range(10):
        x.append(-p+2**i)
    
    n0 = []
    n1 = []
    n2 = []
    n3 = []
    n4 = []
    n5 = []
    n6 = []
    n7 = []
    n8 = []
    n9 = []
    #print x
    toss = []
    gain = []
    winloss = []

    for i in range(2**tosses):
       toss.append(('{:0%db}'%tosses).format(i))


    for i in toss:
        value = n-p
        cons = 0
        for j in i:
            if j == '0':
                value = value - p + 1
                cons = 0
            if j == '1':
                cons = cons + 1
                value = value + 2**(cons-1)
        if i[-1] == '1':
            value = value + 1
        gain.append(value)        
        winloss.append(int(math.copysign(1,value)))



    print float(winloss.count(1))/(len(winloss))



    neg = list(combinations(n0, 3))
    pos = list(combinations(n0, 3))
    
    
    
    
    
    
    
    
    
    
    """for y in range(2*n,10*n,100):
        count = 0
        count2 = 0
        for i in neg:
            if 6*i[0] + 3*i[1] + i[2] > y:
                count = count + 1
        for j in neg:
            if n + j[0] + 9*j[1] + 25*j[2] <= y:
                count2 = count2 + 1
        print y, count, count2, (count//300)*(count2//300)    
        for j in pos:
            if 6*i[0] + 3*i[1] + i[2] > n + j[0] + 9*j[1] + 25*j[2]:
                print i, j
                count = count + 1
    
    print count, count2, (count//300)*(count2//300)"""
    
    
    
    
    """infin = 1
    games = 0    
    while games < 100000:
        i = starting_tokens - p
        wins = 1
        ntoss = 0
        while i > p and ntoss < 100000:
            toss = randint(0, 1)
            if toss == 1:
                wins = wins+1
            else:
                i = i + 2**wins - p
                wins = 0
            ntoss = ntoss + 1 
        if i > p:
           infin = infin + 1
        games = games + 1
        print games"""
        
        
        
        
        
        
    """ while n[-1] > cost and len(n) < 100:
        i = i+1 
        x =  (n[i-1] - cost + 1)/2 + (n[i-1] + 2^i)/2
        n.append(x)"""
        
                         
        
    return 0

print solution(7, 30)