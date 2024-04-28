# 별자리 만들기

import sys
import enum


class Position(enum.IntEnum):
    X = 1
    Y = 0


# 입력 받기
n = int(sys.stdin.readline())

loc = [[0,0] for i in range(n)]
for i in range(n):
    loc[i][Position.X], loc[i][Position.Y] = map(float, sys.stdin.readline().split())


# Kruskal MST 를 구할 것이다.
edges = []
for i in range(n):
    for j in range(i+1, n):
        # 서로 다른 두 노드간 거리 구하기 (거리 = 간선의 가중치로 본다)
        dx = loc[i][Position.X] - loc[j][Position.X]
        dy = loc[i][Position.Y] - loc[j][Position.Y]
        w = (dx**2 + dy**2)**0.5
        edges.append((w, i, j))

parent = [*range(n)]

def find(i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(i, j):
    i = find(i)
    j = find(j)
    if i > j:
        i, j = j, i
    parent[j] = i

total_w = 0
for w, i, j in sorted(edges):
    i = find(i)
    j = find(j)
    if i == j:
        continue
    union(i, j)
    total_w += w

sys.stdout.write(f"{total_w}\n")
