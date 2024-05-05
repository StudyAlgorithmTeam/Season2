V,E = map(int, input().split())
Varr = []
parent = list(range(V+1))
w = 0

def find(x):
    while x != parent[x]:
        x = parent[x] # 같으면 부모값이 가리키는 값으로 바꿔줌 최종적으로는 조상 값을 가지게 됨
    return x

def union(u,v):
    u = find(u)
    v = find(v)
    if u < v:
        u,v = v,u
    parent[u] = v

for _ in range(E):
    a, b, c = map(int,input().split())
    Varr.append((c,a,b))

Varr.sort()
print(Varr)


for c,a,b in Varr:
    a = find(a) 
    b = find(b)
    if a!=b:
        print(c)
        union(a,b)
        w = w + c

print(c)