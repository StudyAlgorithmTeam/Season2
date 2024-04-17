import collections
import sys


MAX_N = 100

N, M, R = map(int, sys.stdin.readline().split())
T = [None] + [*map(int, sys.stdin.readline().split())]

graph = collections.defaultdict(list)
for i in range(R):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a].append((b, l))
    graph[b].append((a, l))


def dijkstra(root: int):
    dist = [sys.maxsize] * (N+1)
    dist[root] = 0
    q = collections.deque([root])
    while q:
        u = q.popleft()
        for v, d in graph[u]:
            if dist[v] > dist[u] + d:
                dist[v] = dist[u] + d
                q.append(v)
    return sum(T[i] for i in range(1, N+1) if dist[i] <= M)


answer = max(dijkstra(i) for i in range(1, N+1))
print(answer)
