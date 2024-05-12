# 최단경로

import heapq
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

dist = [sys.maxsize] * (V+1)
dist[K] = 0

pq = [(0, K)]
while pq:
    d, u = heapq.heappop(pq)
    if d <= dist[u] and u in cost:
        for v in cost[u]:
            if dist[v] > dist[u] + cost[u][v]:
                dist[v] = dist[u] + cost[u][v]
                heapq.heappush(pq, (dist[v], v))

for i in range(1, V+1):
    if dist[i] == sys.maxsize:
        sys.stdout.write("INF\n")
    else:
        sys.stdout.write(f"{dist[i]}\n")
