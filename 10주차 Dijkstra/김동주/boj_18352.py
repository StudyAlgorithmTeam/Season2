# 특정 거리의 도시 찾기

from collections import defaultdict
from collections import deque
import sys


N, M, K, X = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)

answers = set()

# Dijkstra
dist = [sys.maxsize] * (N+1)
dist[X] = 0
q = deque([X])
while q:
    u = q.popleft()
    if dist[u] == K:
        answers.add(u)
        continue
    for v in graph[u]:
        if dist[v] > dist[u]+1:
            dist[v] = dist[u]+1
            q.append(v)


if len(answers) == 0:
    sys.stdout.write("-1")
else:
    sys.stdout.write("\n".join(map(str, sorted(answers))))
