#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 20:58:22 2017

@author: Seyed
"""

import math
import itertools
import csv
import timeit

start = timeit.default_timer()


def solution(tuple_of_points):
   t = tuple_of_points
   n= len(t)
   Area = 0
   tc = tuple(itertools.combinations(t,2)) #tc is the collection of all the segments
   #dic2 is the dictionary where the keys are the slopes and the values are the
   #coordinates of the endpoints of the segments
   dic2 = {}

   
   for x in tc:
       if x[1][0]-x[0][0] != 0: #Check if the slope is not infinity
               slope = float(x[1][1]-x[0][1])/(x[1][0]-x[0][0]) #Calculate slope and add the segment to the relevant key
               if not slope in dic2:
                   dic2[slope] = [x]
               else:
                   dic2[slope].append(x)
       else:                        #Same procedure for the infinite slopes
          if not 'inf' in dic2:
              dic2['inf'] = [x]
          else:
              dic2['inf'].append(x)  
  

    #For every slope, take combinations of all the segments and calculate the area of the trapeziums
    #using the formula 0.5|x1y2 + x2y3 + x3y4 + x4y1 - x2y1 - x3y2 - x4y3 - x1y4|
    #We just need to check the order of the points before doing the calculations since we need to go in a circular-wise order
    # The final if-else is to check whether the lengths of the two segments are equal, if yes, then it is a parallelogram
    # and we are calculating the same area twice. Hence in this case, we only calculate half of it's area to avoid double calculating
   for i in dic2:
        if (len(dic2[i]))>1:
            zc = tuple(itertools.combinations(dic2[i], 2))
            l=len(zc)
            for j in range(l):
                if ((zc[j][0][0][0]-zc[j][0][1][0])*(zc[j][1][0][0]-zc[j][1][1][0])<0)or ((zc[j][0][0][1]-zc[j][0][1][1])*(zc[j][1][0][1]-zc[j][1][1][1])<0):
                    A = 0.5*abs(((zc[j][0][0][0])*zc[j][0][1][1]+zc[j][0][1][0]*zc[j][1][0][1]+zc[j][1][0][0]*zc[j][1][1][1]+zc[j][1][1][0]*zc[j][0][0][1]-zc[j][0][1][0]*zc[j][0][0][1]-zc[j][1][0][0]*zc[j][0][1][1]-zc[j][1][1][0]*zc[j][1][0][1]-zc[j][0][0][0]*zc[j][1][1][1]))
                else:
                    A = 0.5*abs(((zc[j][0][1][0])*zc[j][0][0][1]+zc[j][0][0][0]*zc[j][1][0][1]+zc[j][1][0][0]*zc[j][1][1][1]+zc[j][1][1][0]*zc[j][0][1][1]-zc[j][0][0][0]*zc[j][0][1][1]-zc[j][1][0][0]*zc[j][0][0][1]-zc[j][1][1][0]*zc[j][1][0][1]-zc[j][0][1][0]*zc[j][1][1][1]))
                if (zc[j][0][0][0]-zc[j][0][1][0])**2 + (zc[j][0][0][1]-zc[j][0][1][1])**2 == (zc[j][1][0][0]-zc[j][1][1][0])**2 + (zc[j][1][0][1]-zc[j][1][1][1])**2:
                    Area = Area + A/2
                else:
                    Area = Area + A


   
   return int(Area * 1000)




x = []
with open('input.txt','r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        x.append([int(row[0]),int(row[1])])
      
y = tuple(x)
print solution(y) 
    
    
    
   
stop = timeit.default_timer()

print stop - start    
     