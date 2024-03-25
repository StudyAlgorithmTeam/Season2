import sys
input = sys.stdin.readline
from itertools import permutations
T = int(input())
rarr = []
for j in range(T):
    n,m = map(int,input().split())
    narr = list(map(int,input().split()))
    marr = []
    RR = []
    for i in range(m):
        x,y = map(int,input().split())
        marr.append((x,y))


    for comb in permutations(narr,len(narr)):
        result = []
        result.append(comb[0])
        for i in range(1,len(comb)):
            a = result[i-1] + comb[i]
            result.append(a)
        result.insert(0,0)
        a = 0
        for j in marr:
            a += result[j[1]]-result[j[0]-1]
        RR.append(a)
    RR.sort()
    RR.reverse()
    b = []
    for i in range(len(RR)-1,0,-1):
        if RR[0] == RR[i]:
            b.append(i+1)
            break

    if b:
        rarr.append((RR[0],b[0]))
    else:
        rarr.append((RR[0],1))

for i in rarr:
    x=i[0]
    y=i[1]
    print(x,y)
