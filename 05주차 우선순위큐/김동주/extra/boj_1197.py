from sys import stdin
from sys import stdout
from typing import List


NO_PARENT = -1


def find(i: int, parent: List[int]):
    if parent[i] == NO_PARENT:
        return i
    parent[i] = find(parent[i], parent)
    return parent[i]


def union(x: int, y: int, parent: List[int], rank: List[int]):
    px = find(x, parent)
    py = find(y, parent)
    if px == py:
        return
    if rank[px] == rank[py]:
        parent[py] = px
        rank[px] += 1
        return
    if rank[px] > rank[py]:
        px, py = py, px
    parent[px] = py


def testcase(tid):
    V, E = map(int, stdin.readline().split())

    edges = []
    for i in range(E):
        A, B, C = map(int, stdin.readline().split())
        edges.append((C, A, B))
    edges.sort()

    parent = [NO_PARENT] * (V+1)
    rank = [1] * (V+1)
    answer = 0

    for w, u, v in edges:
        if find(u, parent) != find(v, parent):
            union(u, v, parent, rank)
            answer += w

    stdout.write(str(answer))
    stdout.write('\n')


if __name__ == '__main__':
    # T = int(stdin.readline())
    # for tid in range(1, T+1):
    #     testcase(tid)
    testcase(0)
