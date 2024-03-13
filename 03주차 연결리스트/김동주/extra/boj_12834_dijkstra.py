import collections
import heapq
import sys
import typing


INF = -1

N, V, E = map(int, sys.stdin.readline().split())
A, B = map(int, sys.stdin.readline().split())
H = list(map(int, sys.stdin.readline().split()))

graph: typing.Dict[int, typing.List[int]] = collections.defaultdict(list)

for i in range(E):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a].append((l, b))
    graph[b].append((l, a))

def bfs(start: int, dist: typing.List[int]):
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if dist[u] == INF or dist[u] > d:
            dist[u] = d
            for w, v in graph[u]:
                heapq.heappush(pq, (dist[u]+w, v))

dist_A = [INF] * (V+1)
dist_B = [INF] * (V+1)

bfs(A, dist_A)
bfs(B, dist_B)

print(sum(dist_A[H[i]]+dist_B[H[i]] for i in range(N)))
