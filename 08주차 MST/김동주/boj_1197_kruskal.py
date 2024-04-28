from typing import *
import sys


N: int
parent: List[int]


def find(i: int) -> int:
    while i != parent[i]:
        i = parent[i]
    return i


def union(i: int, j: int) -> int:
    i = find(i)
    j = find(j)
    if i < j:
        i, j = j, i
    parent[i] = j


if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    parent = [*range(V+1)]
    edges = [tuple(map(int, sys.stdin.readline().split())) for i in range(E)]
    total_w = 0
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        u = find(u)
        v = find(v)
        if u != v:
            union(u, v)
            total_w += w
    sys.stdout.write(f"{total_w}\n")
