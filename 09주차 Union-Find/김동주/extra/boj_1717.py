# 집합의 표현

from typing import *
import sys


MAX_N = int(1e6)

n, m = map(int, sys.stdin.readline().split())

parent = list(range(n+1))


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        a, b = b, a
    parent[a] = b


sys.setrecursionlimit(MAX_N)

for i in range(m):
    cmd, a, b = map(int, sys.stdin.readline().split())
    if cmd == 0: # union
        union(a, b)
    if cmd == 1: # check
        a = find(a)
        b = find(b)
        if a == b:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
