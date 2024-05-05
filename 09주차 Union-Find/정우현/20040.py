import sys
input = sys.stdin.readline

N,M = map(int,input().split())
Varr = []

parent = list(range(N)) #range 자체가 이터러블이고 0부터 i까지 1씩 증가시켜준다.
count = 0

def find(i):
    while i != parent[i]:
        i = parent[i]
    return i

def union(u,v):
    if u < v:
        u,v = v,u
    parent[u] = v #더 작은 값을 넣어준다.
    

for _ in range(M):
    u,v = map(int,input().split())
    Varr.append((u,v))

is_in = 0

for u,v in Varr:
    count += 1
    if u == v:
        break
    u = find(u)
    v = find(v)
    if u!= v:
        union(u,v)
    else:
        is_in = 1
        break
        
    

if count == len(Varr) and is_in == 0:
    print(0)
else:    
    print(count)

#find는 부모 값을 찾는 것 parent [0,0,]
#union은 배열에 넣는 것