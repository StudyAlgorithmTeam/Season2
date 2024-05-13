import sys


n, m = map(int, sys.stdin.readline().split())

parent = [*range(n)]


def find(i):
    while parent[i] != i:
        i = parent[i]
    return i


def union(i, j):
    i = find(i)
    j = find(j)
    if i < j:
        i, j = j, i
    parent[i] = j


for i in range(1, m+1):
    u, v = map(int, sys.stdin.readline().split())
    u = find(u)
    v = find(v)
    if u == v:
        # 사이클 발견
        sys.stdout.write(f'{i}\n')
        break
    union(u, v)
else:
    # 종료되지 않음
    sys.stdout.write('0\n')
