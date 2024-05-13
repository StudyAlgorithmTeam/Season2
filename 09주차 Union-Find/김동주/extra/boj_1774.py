# 우주신과의 교감

import sys


N, M = map(int, sys.stdin.readline().split())
X = [0] * (N+1)
Y = [0] * (N+1)
parent = list(range(N+1))
edges = []
for i in range(1, N+1):
    X[i], Y[i] = map(int, sys.stdin.readline().split())
    for j in range(1, i):
        w = ((X[j]-X[i])**2+(Y[j]-Y[i])**2)**0.5
        edges.append((w, i, j))
edges.sort()

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    while i != parent[i]:
        i = parent[i]
    while j != parent[j]:
        j = parent[j]
    if i < j:
        i, j = j, i
    parent[i] = j

total_w = 0
for w, i, j in edges:
    while i != parent[i]:
        i = parent[i]
    while j != parent[j]:
        j = parent[j]
    if i == j:
        continue
    if i < j:
        i, j = j, i
    parent[i] = j
    total_w += w

sys.stdout.write(f"{total_w:.2f}\n")
