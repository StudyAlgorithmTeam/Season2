# 벽 부수고 이동하기 2

from collections import deque
from typing import List
import sys


N, M, K = map(int, sys.stdin.readline().split())
GRID = sys.stdin.readlines()


def is_in_grid(n: int, m: int) -> bool:
    return 0 <= n and n < N and 0 <= m and m < M


def is_wall(n: int, m: int) -> bool:
    return is_in_grid(n, m) and GRID[n][m] == '1'


dist: List[List[List[int]]] = []
for y in range(N):
    dist.append([])
    for x in range(M):
        dist[y].append([ sys.maxsize ] * (K+1))

q = deque([(0, 0, 0)])
dist[0][0][0] = 1


def is_visitable(n: int, m: int, k: int) -> bool:
    return is_in_grid(n, m) and 0 <= k and k <= K


def visit(n: int, m: int, k: int, d: int) -> None:
    if is_wall(n, m):
        k += 1
    if is_visitable(n, m, k) and dist[n][m][k] > d+1:
        dist[n][m][k] = d+1
        q.append((n, m, k))


while q:
    n, m, k = q.popleft()
    d = dist[n][m][k]
    if n == N-1 and m == M-1:
        break
    visit(n-1, m, k, d)
    visit(n+1, m, k, d)
    visit(n, m-1, k, d)
    visit(n, m+1, k, d)


d = min(dist[N-1][M-1])
if d == sys.maxsize:
    print(-1)
else:
    print(d)
