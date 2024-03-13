import collections
import heapq
import sys


graph = collections.defaultdict(list)

n, m = map(int, sys.stdin.readline().split())
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
s, t = map(int, sys.stdin.readline().split())

dist = [sys.maxsize] * (n+1)
pq = [(0, s)]
while pq:
    d, u = heapq.heappop(pq)
    if dist[u] > d:
        dist[u] = d
        for w, v in graph[u]:
            heapq.heappush(pq, (d+w, v))

print(dist[t])
