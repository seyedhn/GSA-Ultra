#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 23:17:16 2017

@author: Seyed
"""
import itertools
from compiler.ast import flatten
import copy
# Please write your code inside the function stub below.
def solution1(n, m, k, v):
    count=0
    for i in range(v,(2**n)+1):
        f_k=0
        j=bin(i|(1<<n))[3:]
        for l in range(n-k+1):
            fk=int(j[l:l+k],2)
            if fk>=v:
                f_k+=1
        if f_k>=m:
            count+=1
    
    xx = [0,1]
    for y in range(2,m+1):
        xx.append(2*xx[y-1]+2**(y-2))
    
    yy=0
    if k < m + len(bin(v))-2:
        yy = (n+1-k-m)*v
 
                 
    
 
    x = 2**n - xx[m]*(v) - yy
    #print 2**n - xx[5]*v           
    return count 

#print solution1(24,12,10,123)





def solution2(n, m, k, v):

    shared = []
    every = []
    count = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    
    for i in range(v,2**k):
       shared.append(('{:0%db}'%k).format(i))
       
    for i in range(2**k):
       every.append(('{:0%db}'%k).format(i))   
       
    """for i in shared:
        for j in shared:
            for l in shared:
                for m in shared:
                    if (str(i)[:-1] == str(j)[1:] and str(j)[:-1] == str(l)[1:] and str(l)[:-1] == str(m)[1:]):
                        count = count + 1

                #if str(i)[:-1] == str(j)[1:]  and str(j)[:-1] == str(l)[1:]:
                    #count5 = count5 + 1
                if str(i)[:-1] == str(j)[1:]  and str(j)[:-1] == str(l)[1:]:
                    count5 = count5 + 1  
                if str(i)[:-1] == str(j)[1:] and str(j)[:-2] == str(l)[2:]:
                    count6 = count6 + 1
                if str(i)[:-2] == str(j)[2:] and str(j)[:-1] == str(l)[1:]:
                    count3 = count3 + 1  
                    
                #if str(i)[:-3] == str(j)[3:] and str(j)[:-2] == str(l)[2:]:
                    #count7 = count7 + 1 
    haha = [0]*10
    haha2 = [0]*10
    haha3 = []
    haha4 = [0]*10   
    """

    countnum = {}

    alldics =  [dict() for x in range(k)]
    allnums =  [dict() for x in range(k)]
       
    """for i in range(len(shared)):
        for j in range(len(shared)):
                if str(shared[i])[:-1] == str(shared[j])[1:]:
                    dic[i] = j
                    count2 = count2 + 1
                    haha[j]  = haha[j] + 1
                    haha2[i] = haha2[i] + 1

                if str(shared[i])[:-2] == str(shared[j])[2:]   :
                    count4 = count4 + 1
                    #haha3[j]  = haha3[j] + 1
                    haha4[i] = haha4[i] + 1
                if str(shared[i])[:-3] == str(shared[j])[3:]   :
                    count7 = count7 + 1
    for i in range(len(haha3)):
       for j in range(len(shared)):
               if str(haha3[i])[:-1] == str(shared[j])[1:]:
                       haha4[j] = haha4[j] + 1"""
    for l in range(1,k):             
        for i in shared:
            for j in shared:
                if str(i)[:-l] == str(j)[l:]:  
                    if not i in alldics[l]:
                        alldics[l][i] = [j]
                        allnums[l][i] = 1
                        countnum[i] = 0
                    else:
                        alldics[l][i].append(j)
                        allnums[l][i] = allnums[l][i] + 1 
                               
        #print i, dic[i]
    """ccc = 0
    for i in dic:
        for j in dic[i]:
            ccc = ccc + sum(len(dic[x]) for x in dic[j])"""
            
      
    """def func(c):
        x = []
        for i in flatten(c):
            x.append(dic[i])
        return x"""
    
    
    def func2(c, l):
        #dic3 = dict(dic2)
        dic3 = allnums[l].copy()
        for i in c:
            dic3[i] = 0
            for j in alldics[l][i]:
                
                #dic3[i] = (dic2[i] + dic2[j])
                dic3[i] = dic3[i] + allnums[l][j]
        for i in allnums[l]:
            allnums[l][i] = dic3[i]

    """def func2(c, l):
        #dic3 = dict(dic2)
        dic3 = countnum.copy()
        for i in c:
            dic3[i] = 0
            for j in alldics[l][i]:
                
                #dic3[i] = (dic2[i] + dic2[j])
                dic3[i] = dic3[i] + allnums[l][j]
        for i in countnum:
            countnum[i] = dic3[i]"""

      
    #print len(func(func(func(func(func(list(dic.keys()))))  )))
    i = 2
    while i< m:
        #func2(list(allnums[1].keys()), 1)
        i = i + 1

    func2(list(allnums[3].keys()), 3)
    func2(list(allnums[3].keys()), 3)
    func2(list(allnums[3].keys()), 3)


    print (sum(allnums[3][i] for i in allnums[3]))

    print (sum(allnums[1][i] for i in allnums[1])*(n-k-m+2)*2**(n-k-m+1))%1000000007
    #print sum(haha[i]*haha2[i]*haha2[i] for i in range(10))
    #print sum(haha[i]*haha2[i]*haha4[i] for i in range(10))
    """for i in every:
        for j in every:  
            for k in every:
                if str(i)[:-2] == str(j)[2:] and str(j)[:-1] == str(k)[1:] and int(i) >= v and int(j) >=v and int(k)<v:
                    count2 = count2 + 1
                   # print str(k)+str(i[-1])
                if str(i)[:-2] == str(j)[2:] and str(j)[:-1] == str(k)[1:] and int(i) >= v and int(j) <v and int(k)>=v:
                     count2 = count2 + 1
                    
                if str(i)[:-2] == str(j)[2:] and str(j)[:-1] == str(k)[1:] and int(i) < v and int(j) >=v and int(k)>=v:
                     count2 = count2 + 1
                    
                if str(i)[:-2] == str(j)[2:] and str(j)[:-1] == str(k)[1:] and int(i) >= v and int(j) >=v and int(k)>=v:
                     count3 = count3 + 1"""
                     
                     
      # 2*(int(n)-int(k)-1)   
    #print (41*(1676**50)*2**41)%1000000007
     #This is the case for m = 2, N - k = 2 
    #print -2*count + 4*count2  + 1*count4  
    
    
    
    #This is the case for m = 2, N - k = 3 
   # print 12*count2 + 4*count4 + count7 - 8*count5 - 2*count6 -2*count3 + 3*count

    
    #This is the case for m = 3, N - k = 2 
    #print 4*count5 + count6 + count3 - 3*count
    
    
    
    #return count2,  count4, count7, count5, count6, count, count3
    return
print solution2(10, 3, 4, 6) 

"""def solution3(n, k, v):

    st = []
    count2 = 0
    st2 = []
    
    for i in range(v,2**k):
       st.append(('{:0%db}'%k).format(i))
       
    print len(st)
    for kk in range(1,k):    
        for i in st:
            for j in st:
                    if str(i)[:-k] == str(j)[k:]:
                        st2.append(str(j)[0:k-1] + str(i))


    print len(st2)"""


def solution4(n,m,k,v):
    
    bigger = [] #The list of all binary strings greater than v
    
    for i in range(v+1,2**k):   #Add all the binary strings greater than v to 'bigger'
       bigger.append(('{:0%db}'%k).format(i))
       
       
    dic = {}    #The key will be the strings in 'bigger' . The values are the next contiguous strings which are also from bigger
    dicnum = {} #dicnum stores the number of substrings from bigger than can be placed next to the key strings by one space
    
             #Fill the dictionaries with all strings bigger than v and the values with all those that can be placed next to them
    for i in bigger:
        for j in bigger:
            if str(i)[:-1] == str(j)[1:]:  
                if not i in dic:
                    dic[i] = [j]
                    dicnum[i] = 1
                else:
                    dic[i].append(j)
                    dicnum[i] = dicnum[i] + 1   
                          
    #The function func will add to dicnum accordingly if we connect 3 contiguous substrings each by 1 space
    def func(c):
        dic3 = dicnum.copy()
        for i in c:
            dic3[i] = 0
            for j in dic[i]:
                dic3[i] = dic3[i] + dicnum[j]
        for i in dicnum:
            dicnum[i] = dic3[i]

    #Perform func for m contiguous substrings which fills dicnum up to m
    i = 2   
    while i< m:
        func(list(dicnum.keys()))
        i = i + 1
    
    
    i = [22657, 62665]
    for x in range(37):
        i.append(2*(i[x]+i[x+1]))
    print i[-1]
    
    #sum of all the values of dicnum is the total number of possibilities for m contiguous substrings
    #of length k which are greater than v
    #This leaves (n-k-m+2) different positions in the whole string to put the m contiguous ones
    #Also all the remaining slots can take up to 2^(n-k-m+1) different values
    print (sum(dicnum[i] for i in dicnum)*(n-k-m+2)*2**(n-k-m+1))%1000000007
    print (sum(dicnum[i] for i in dicnum))

print solution4(100, 50, 10, 124) 

