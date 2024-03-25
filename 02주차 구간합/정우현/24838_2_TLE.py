import math
import sys
input = sys.stdin.readline
T = int(input())
rarr = []
#결과를 저장하는 배열

for _ in range(T):
    n,m = map(int,input().split())
    narr = list(map(int,input().split()))
    narr.sort()
    narr.reverse()
    result = [0]*n
    #구간에서 곂치는 부분이 얼마나 있는지 알려주는 배열

    #구간 마다 1씩 더해준다
    for i in range(m):
        x,y = map(int,input().split())
        for j in range(x-1,y):
            result[j] += 1

    result.sort()
    result.reverse()
    RR = 0

    #최대값
    for o in range(len(result)):
        RR += result[o]*narr[o]

    #곂치는 부분의 개수
    count = {}
    RRR = []
    for i in result:
        try:
            count[i] += 1
        except:
            count[i] = 1
        
    for key in count:
        RRR.append(count[key])

    rrr = 1
    for k in RRR:
        rrr *= math.factorial(k)
    rarr.append((RR,rrr))
for i in rarr:
    print(i[0],i[1])
