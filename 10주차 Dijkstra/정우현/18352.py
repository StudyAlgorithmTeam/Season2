import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
g = [[] for _ in range(N + 1)]
v = [0] * (N + 1) 

for _ in range(M):
    x, y = map(int, input().split())
    g[x].append(y)

def bfs(z):
    q = []
    q.append((z, 0))
    v[z] = 1
    while q:
        now, n = q.pop(0)
        if n == K:
            a.append(now)
        elif n > K:
            return
        for i in g[now]:
            if v[i] == 0:
                v[i] = 1
                q.append((i, n + 1))  

a = []
bfs(X)
if not a:
    print(-1)
else:
    a.sort()
    print(*a, sep="\n")
