#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 09:42:28 2017

@author: Seyed
"""


import itertools

def solution(tuple_of_integers):
    t = tuple_of_integers
    n = len(t)
    x = [] # x is the list which contains the number of possibilities for each combination of possible list titles
    #We first need to check the index of the first list which begins with -1. We call it indexfirst
    y = 0 #y is the number of -1's before the first corrupted list   
       
    i = 0
    firstindex = -1
    while i < n and firstindex == -1:
        if t[i] == -1:      #If the item is -1, then this is the first corrupted list title
            firstindex = i           
        else:
            i = i + t[i]+1  #If not, skip by the list size and check the next list
    
    #Once the first corrupted list title is found, the number of possibilities so far will be 1001 to the power of number of -1's
    # that existed before the first corrupted list title
    y = t[:firstindex].count(-1)
    
    
    #From now on, we do not care about all the entries before the first corrputed list title
    #Hence we only take take the part of the data after we find the first corrupted list title
    t = t[firstindex:]
    n = len(t[firstindex:])
    index = []  #index is the list of the indecies of our data
    combs = []  # combs is the list containing all the combinations of list title positions
    
    
    #Create the list of the index of possible title positions of extra lists.
    for i in range(n):
        index.append(i)    

    for L in range(1,n): #L is the number of lists that can be in the data. We count from 1 to n possible lists
        for i in list(itertools.combinations(index[1:],L)): #We skip index 0 because it's a corrupted list title anyways.
                combs.append(i)
          
    
    #For the case that there exists only one list
    x.append((1001**(t.count(-1)-1+y)))
   
    #For the cases of multiple lists, check all the combinations in combs
    for i in combs:
        cnt = 0
        for j in i:
            if t[j] == -1:  #Count how many lists titles are -1
                cnt = cnt + 1
        #If All the list titles correctly represent the number of their entries or are -1 (the part after 'and' is the same thing for checking the last last)
        #Then count the number of the -1's that appear everywhere except in the list titles and add the number of possibilities to x
        if all(t[i[j]] == i[j+1] - i[j] - 1 or t[i[j]] == -1  for j in range(len(i)-1)) and (t[i[-1]] == n-i[-1]-1 or  t[i[-1]] == -1):
            print i
            x.append((1001**(t.count(-1)-1-cnt+y)))


    return sum(x)

print solution((-1,2,3,-1,4,5,-1,6,7,-1))%1000000007           
              
              
              
              
              