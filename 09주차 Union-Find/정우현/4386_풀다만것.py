import math

n = int(input()) #별의 개수
Varr =[] #별의 좌표 저장하는 배열
parent = list(range(n))

def find(x):
    while x!=parent[x]:
        x = parent[x]
    return x

def union(u,v):
    if u<v:
        u,v = v,u
    parent[u] = v



for _ in range(n):
    x,y = map(float,input().split())
    w= x+y
    Varr.append((x,y,w))

Varr.sort(key = lambda x:x[2])
length = 0



for i in range(len(Varr)-1):
    x = Varr[i][0]
    y = Varr[i][1]
    n_x = Varr[i+1][0]
    n_y = Varr[i+1][1]

    length += math.sqrt((x-n_x)**2 + (y-n_y)**2)

print(length,2)

#방법 1 각 좌표마다 다른 별에 가는데 드는 비용을 계산 작은 걸로 하는데 
#방문한지 체크 그리고 작은 값을 위주로 넣는다.n곱하기 n배열과 parent 배열
#두개가 필요할 듯
#거리 계산 따로 사이클 체크 따로 