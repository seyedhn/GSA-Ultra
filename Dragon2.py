#Please write your code inside the function stub below.
def solution(tuple_of_painting_coords):
    t = [list(key) for key in tuple_of_painting_coords]
    del tuple_of_painting_coords

    n = len(t)
    count = 0
    det = lambda A, B, C: (A[0] - B[0]) * (C[1] - A[1]) - (A[1] - B[1]) * (C[0] - A[0])
    norm = lambda A: min(abs(A[0]) + abs(A[1]), abs(A[2]) + abs(A[3]))
    ntwo = lambda A: A[0]*A[0] + A[1]*A[1]
    dotp=lambda A,B: A[0]*B[0] + A[1]*B[1]
    tmin=lambda A,B: (2*ntwo(B)-dotp(A,B))/(2*ntwo(A)+2*ntwo(B)-2*(dotp(A,B)))
    def dist(seg):
        A=[seg[0],seg[1]]
        B=[seg[2],seg[3]]
        t=tmin(A,B)
        if t<=1 and t>=0:
            return ntwo([t*A[0]+(1-t)*B[0],t*A[1]+(1-t)*B[1]])
        else:
            return min(ntwo(A),ntwo(B))

    for i, key in enumerate(t):
        if (key[0]*key[3]-key[2]*key[1]) > 0:  # in case of <0 the point key[0:2] has higher slope from origin (0,0) or the triangle(key[0:2],key[2:],(0,0)) is anticlockwise

            t[i] = [key[2], key[3], key[0], key[1]]
    def inverse(a, b, c, d):
        if (a * d - b * c)!=0:
            return [d / (a * d - b * c), -b / (a * d - b * c), -c / (a * d - b * c), a / (a * d - b * c)]
        else:
            return None

    def orti(p, seg):
        A = inverse(p[2], p[0], p[3], p[1])
        if A!=None:

            seg1 = [A[0] * seg[0] + A[1] * seg[1], A[2] * seg[0] + A[3] * seg[1]]
            seg2 = [A[0] * seg[2] + A[1] * seg[3], A[2] * seg[2] + A[3] * seg[3]]
            if seg1[0] >= 0 and seg1[1] >= 0 and seg2[0] >= 0 and seg2[1] >= 0 and seg1[0] + seg1[1] >= 1 and seg2[0] + \
                    seg2[1] >= 1:
                return 0
            elif seg1[0] >= 0 and seg1[1] >= 0 and seg2[0] >= 0 and seg2[1] <= 0 and seg1[0] + seg1[1] >= 1:
                return 2
            elif seg2[0] >= 0 and seg2[1] >= 0 and seg1[0] <= 0 and seg1[1] >= 0 and seg2[0] + seg2[1] >= 1:
                return 3
            #elif seg1[0] <= 0 and seg1[1] >= 0 and seg2[0] >= 0 and seg2[1] <= 0 and seg2[0] + seg2[1] >= 1 and seg1[0] + \
                    #seg1[1] >= 1:
                #return 4
            else:
                return 1
        else:
            return 1
    def convex(segs):
        ted=len(segs)
        result=list(segs)
        for i in range(ted):
            for j in range(i+1,ted):
                A=segs[i]
                B=segs[j]
                if orti(A,B) ==2 :
                    pass




    def intersection(a, seg):
        data = (a[0] * (seg[0] * seg[3] - seg[1] * seg[2])) / (-a[0] * (seg[1] - seg[3]) + a[1] * (seg[0] - seg[2]))
        data1 = (a[1] * (seg[0] * seg[3] - seg[1] * seg[2])) / (-a[0] * (seg[1] - seg[3]) + a[1] * (seg[0] - seg[2]))
        return [data, data1]

    segs=[]
    while n > 0:
        distancefromzero = {dist(key): i for i, key in enumerate(t)}
        index = distancefromzero[min(distancefromzero)]
        point = t[index]
        count += 1
        segs.append(point)
        t.pop(index)
        n = n - 1
        ind = []
        for i, seg in enumerate(t):
            for point in segs:


                ort = orti(point, seg)
                if ort == 0:
                    ind.append(i)
                elif ort == 2:
                    key = intersection(point[2:], seg)
                    t[i] = [key[0], key[1], seg[2], seg[3]]
                elif ort == 3:
                    key = intersection(point[0:2], seg)
                    t[i] = [seg[0], seg[1], key[0], key[1]]
                #elif ort == 4:
                    #key = intersection(point[2:], seg)
                    #t[i] = [key[0], key[1], seg[2], seg[3]]
                    #key = intersection(point[0:2], seg)
                    #t.append([seg[0], seg[1], key[0], key[1]])

        t = [t[i] for i in range(n) if not (i in ind)]
        n = len(t)

    return count


#tp = ((1, 1, 1, 0), (2, 3, 2, -3),(1,-2,1,-5),(4,0,4,-4),(-2,1,-2,-1), (-3, 7, -3, -8), (-4, 1, -4, -1))
#print(solution(tp))

import csv

x = list()
with open('input3.txt', 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        x.append([int(row[0]), int(row[1]), int(row[2]), int(row[3])])

print(solution(x))

