import collections
import heapq
import sys
import typing


INF = -10000000


N, E = map(int, sys.stdin.readline().split())
graph: typing.Dict[int, typing.List[int]] = collections.defaultdict(list)

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, map(int, sys.stdin.readline().split()))

def dijkstra(start: int, end: int):
    dist = [INF] * (N+1)
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if dist[u] == INF or dist[u] > d:
            dist[u] = d
            for w, v in graph[u]:
                heapq.heappush(pq, (dist[u]+w, v))
    return dist[end]

dist_v1_v2 = dijkstra(v1, v2)

dist_1_v1 = dijkstra(1, v1)
dist_v2_N = dijkstra(v2, N)
case_1 = dist_1_v1+dist_v2_N+dist_v1_v2

dist_1_v2 = dijkstra(1, v2)
dist_v1_N = dijkstra(v1, N)
case_2 = dist_1_v2+dist_v1_N+dist_v1_v2

if case_1 >= 0 and case_2 >= 0:
    ans = min(case_1, case_2)
elif case_1 >= 0:
    ans = case_1
elif case_2 >= 0:
    ans = case_2
else:
    ans = -1

sys.stdout.write(str(ans)+'\n')
