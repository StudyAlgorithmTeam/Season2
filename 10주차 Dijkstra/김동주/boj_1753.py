# 최단경로

from collections import deque
import sys


cost = dict()

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if u not in cost:
        cost[u] = dict()
    if v not in cost[u] or cost[u][v] > w:
        cost[u][v] = w

q = deque([K])
dist = [sys.maxsize] * (V+1)
dist[K] = 0
while q:
    u = q.popleft()
    if u in cost:
        for v in cost[u]:
            if dist[v] > dist[u] + cost[u][v]:
                dist[v] = dist[u] + cost[u][v]
                q.append(v)

for i in range(1, V+1):
    if dist[i] == sys.maxsize:
        sys.stdout.write("INF\n")
    else:
        sys.stdout.write(f"{dist[i]}\n")
