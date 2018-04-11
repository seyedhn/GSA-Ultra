#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 06:45:51 2017

@author: Seyed
"""
from fractions import Fraction

def solution(n, m, d):
    
    """The optimal case which gives the most strength is to take
    a nail from a place with the smallest gap between consecutive nails
    and place it in the middle of the largest gap available. The factor that the 
    strength changes with is the new strength of the smallest gap (which is
    obtained by removing the middle nail) multiplied
    by the new strength of the biggst gap (which is obtained by placing
    the nail in the middle) ,divided by the old strengths of the
    two respectively.
    let's say the samllest strength is for nails 1,2,3
    and we have the bigegst gap between nails 4 and 5.
    small gap old strength = (pos of nail 3 - pos of nail 2)*(pos of nail 2 - pos of nail 1)
    small gap new strength = (pos of nail 3 - pos of nail 1)
    big gap old strength = (pos of nail 5 - pos of nail 4)
    big gap new strength = (pos of nail 5 - new pos of nail 2)*(new pos of nail 2 - pos of nail 4)
    """

    t = [0] + list(d) + [n] #The position of all nails
    maxgap_str = 1
    maxgap_pos = []
    mingap_str = n
    mingap_pos = []
    
    #Find the position and strength of the smallest gap
    for i in range(1,len(t)-1):
        if (t[i+1] -  t[i])*(t[i]-t[i-1]) < mingap_str:
            mingap_str = (t[i+1] -  t[i])*(t[i]-t[i-1])
            mingap_pos = [t[i-1], t[i], t[i+1]]
    
    #Find the position and strength of the biggest gap
    for i in range(len(t)-1):
        if t[i+1] -  t[i] > maxgap_str:
            maxgap_str = t[i+1] -  t[i]
            maxgap_pos = [t[i],t[i+1]]
            
    #Calculate the factor that the strength has changed by
    k =  (mingap_pos[2]-mingap_pos[0])/mingap_str*(maxgap_pos[1]-maxgap_pos[0])**2/4/maxgap_str
    
    return str(k.numerator)+str(k.denominator)





print solution(91, 23, (1,2,3,4,5,17,18,19,23,34,35,36,39,41,42,45,49,50,60,79,80,83,90))