import math
import itertools
import csv
from fractions import Fraction


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------



#1. The answer is in your DNA
def DNA(s, x, y):
    """
    The string we are looking at has 3 parts: a part of s that
    begins at position x unti the end of x, a series of full length s,
    and a final substring of s which ends at position y"""
    
    
    s1 = s[(x % len(s)):]  #s1 is the initial substring
    s2 = s[0:(y % len(s)+1)] #s2 is the final substring
    q = (y // len(s)) - (x // len(s)) - 1  #q is the number of full strings b
    
    #Count how many of each letter appears in the range of x to y
    aa = []
    aa.append(q*s.count('A') + s1.count('A') + s2.count('A'))
    aa.append(q*s.count('C') + s1.count('C') + s2.count('C'))
    aa.append(q*s.count('T') + s1.count('T') + s2.count('T'))
    aa.append(q*s.count('G') + s1.count('G') + s2.count('G'))
    
    #Calculate the letter which appeared the most
    mx = aa[0]
    for i in aa:
        if i >= mx:
            mx = i
   
    if aa.count(mx) > 1:
        return 0
    else:
        return mx


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


#5. A traditional crossword clue
def cryptic():
    pass


    
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#8. I got 99 problems
def 99problems(tuple_of_integers):
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
    x.append((1001**(t.count(-1)-1)))
   
    #For the cases of multiple lists, check all the combinations in combs
    for i in combs:
        cnt = 0
        for j in i:
            if t[j] == -1:  #Count how many lists titles are -1
                cnt = cnt + 1
        #If All the list titles correctly represent the number of their entries or are -1 (the part after 'and' is the same thing for checking the last last)
        #Then count the number of the -1's that appear everywhere except in the list titles and add the number of possibilities to x
        if all(t[i[j]] == i[j+1] - i[j] - 1 or t[i[j]] == -1  for j in range(len(i)-1)) and (t[i[-1]] == n-i[-1]-1 or  t[i[-1]] == -1):
            x.append((1001**(t.count(-1)-1-cnt)))

            

    return sum(x)%1000000007 


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#9. Breaking the net
def breaking_the_net(num):
    
    """
    This is a recursion problem. We need to start from the combinations of the
    four numbers which add up to 5 and recursivly use the obtained values to do the
    same for 6 and so on until we reach 1000. So we start by manually putting
    the values up to num = 4. The index of each list represents the total sum 'num'.
    The list n contains the number of possible combinations for that index.
    m1 is the number of combinations which at least has a 1. We did not create this
    list because we can use this formula: m1[x] = n[x-1]
    The list m12 contains the number of combinations which have at least a 1 or a 2.
    The list m123 contains the number of combinations which have at least one of 1,2 or 3.
    The actual formulea for these numbers are:
    
    
    1.  m1[x] = n[x-1]
    2.  m12[x] = n[x-1] + (n[x-2] - m1[x-2])
    3.  m123[x] = n[x-1] + (n[x-2] - m1[x-2]) + (n[x-3] - m12[x-3])
    4.  n[x] = n[x-1] + (n[x-2]-m1[x-2]) + (n[x-3]-m12[x-3]) + (n[x-4] - m123[x-4])
    
    
    Descriptions:
    1. For a sum of 'num', The number of all combinations which have at least a one
    equals the number of combinations for 'num-1' since they can all be added by one
    
    2. the number of all combinations containing 1 or 2 equals n[x-1] which is the
    number of combs that has at least a one, plus (n[x-2] - m1[x-2]) which is 
    all those combinations which does not have a one but has a two.
    
    3. Same procedure as above, but we need to go as far as counting all those combs
    (n[x-3] - m12[x-3]) that do not have 1 or 2 but have a 3.
    
    4. The total number of combs n[x] equals all n[x-1] which have been added by 1, 
    all n[x-2] which do not have a one and have been added by 2 (to avoid same combinations)
    plus all n[x-3] which do not have a 1 or 2 but are added by 3, and all n[x-4] which
    do not have 1,2 or 3 and have been added by 4.
    """
    
    n   = [0,1,2,3,5] 
    m12 = [0,1,2,2,4]
    m123= [0,1,2,3,4]
    
    for x in range(5,num+1):
        m12.append(n[x-2] - n[x-3] + n[x-1])
        m123.append(n[x-1]+n[x-2]-m12[x-3])
        n.append(n[x-1]+n[x-2]+n[x-4]-m12[x-3]-m123[x-4])
    
    return n[-1]


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#12. Triangles
def triangles(n): 
    
    """The player who receives the game as 0,0,0 coins on vertices loses.
    If Alice gets 0,p,q she wins by removing p and q coins. But if she gets
    it as 1,1,1 then she loses because she has to remove 1 or 1,1 and Bob
    removes the other one or two. If Alice receives it as 1,p,q she can remove
    p-1, q-1 and give it to Bob as 1,1,1. This makes Bob to lose for the reasons explained above.
    This pattern goes all the way to n. So if Alice starts with p,p,p she will lose
    otherwise she wins. The probability of getting p,p,p is (n+1), the +1 is for 
    including 0,0,0. All the other (n+1)^3 combinations she wins. Hence she
    wins for (n+1)**3- (n+1) possible configurations."""
    
    return (n+1)**3- (n+1)


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


#14. Ninja John
def Ninja_John(tuple_of_test_cases):
    pass






#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


#1. Trapeziums
def trapezium(tuple_of_points):
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


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#3. Emma's Lucrative Formula
def Emma(t):
    
    """ When we begin by N substances and we have only one day,
    The number of bottles we need is 2^B because we can put one substance
    out, put B of the substances one in each bottle, 
    combination(B,2) of substances in two bottles,
    combination(B,3) of substance in three bottles and
    combination(B,B) = 1 substance in all bottles.
    The summation of these terms leads to 2^B.
    Now if we have 2 days to do it, we can test sqrt(N) of substances
    the same in day 1, and in the second day test those sqrt(N) approved substances.
    For 3 days this wood be 3rd root of N and so on.
    Hence the equation relating B, D and N is:
    2^B = Dth-Root(N)"""
    
    
    output = ''
    for i in t:
        output = output + str(int((math.ceil(math.log(i[0],2)/i[1]))))
   
    return output


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


#4. The Builder
def builder(n, m, d):
    
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



#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


#6. A Bit Stringy








#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


#7. Shouting array
def shouting_array(n):
     
    """Of the occasions when Bill shouts yes is when all four numbers
    are different.This happens combination(n,4) = n*(n-1)*(n-2)*(n-3) times.
    Another possibility is that 3 of the numbers are same and one is different.
    This happens 4n(n-1) times. The 4 takes care of different permutations.
    Hence the total number of possibilities is n*(n-1)*4 + n*(n-1)*(n-2)*(n-3)"""
    
    return n*(n-1)*4 + n*(n-1)*(n-2)*(n-3)


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


#10. Charlie's Fair Game

def Charlie(cost,starting_tokens):
    
    """Let y be our stochastic variable. Then after n times playing, we want
    starting_tokens + y1 + y2 + ... + y_n - np > p
    Dividing this equation by n and taking the limit to infinite gives us
    (y1 + y2 + ... + yn)/n > p
    
    the lhs is the average of y which is the y itself. Hence we 
    are looking for the condition that y > p.
    For the case of p = 7, this only happens if we gain 8, 16, 32 .... coins in each game.
    The sum of these probabilities is
    1/16 + 1/32 + 1/64 + ... = 1/8 """
    

    n=int(math.ceil(math.log(cost,2)))
    if starting_tokens < cost:
        return "00000"
    else:
        return "0"+str(int((float(1)/(2**n))*100000))



#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#11. Cool Sequences
def cool_sequences(n):

    """In calculating this, let's we have a sequence of all integers
    from 1 to n. This is not a cool sequence so we need to eliminate numbers.
    All the prime numbers in the second half of the string can be
    included as they can neither be divided by 2 nor their double exists.
    So we start from the end of the sequence, checking the numbers one by one
    all the way down to n/2.
    If the number is divisible by 2, we increase the count by 1 and check
    the dividend. If it's divisible by 2 again, we continue the same procedure
    until it is not divisible anymore.
    E.g when checking 12, we get  12, 6, 3 and it stops. The count is 3.
    Now if the count is odd, it is best to remove the even-indexed ones to get the maximum length.
    For example above, we remove 6 which is the second number. If we had 5 of them, we had to
    remove second and fourth which would leave us with 3 numbers.
    Hence for those numbers, we get int(count/2) + 1 of lengths and there
    is only one such longest combination, hence W is not effected.
    If the count is even, there are count/2+1 ways of getting the longest
    sequence of length count/2.
    E.g for number 8, we have 8,4,2,1. Count is 4. The longest possible sequence
    is count/2 = 2. There are count/2+1 = 3 ways of getting the longest sequence:
    1,4 ; 2,8 ; 1,8."""

    
    L = 0
    W = 1
    
    for i in range(n, int(n/2),-1):
        count = 1
        j = i
        while j%2 == 0:
            count = count + 1
            j = j/2
        if count%2 == 0:
            W = W*(count/2+1)
            L = L + count/2
        else:
            L = L + int(count/2) + 1
        
    print L
    print W
    
    return str(L)+str(W)
    

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


#13. Dani's dragons










#------------------------------------------------------------------------------
#------------------------------------------------------------------------------







