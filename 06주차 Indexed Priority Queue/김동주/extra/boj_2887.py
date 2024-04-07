import sys


def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, u, v):
    if (u := find(parent, u)) < (v := find(parent, v)):
        u, v = v, u
    parent[u] = v


def testcase(tid):
    N = int(sys.stdin.readline())

    X = []
    Y = []
    Z = []
    for i in range(N):
        x, y, z = map(int, sys.stdin.readline().split())
        X.append((x, i))
        Y.append((y, i))
        Z.append((z, i))
    X.sort()
    Y.sort()
    Z.sort()

    edges = []
    for A in (X, Y, Z):
        for i in range(N):
            j = (i+1) % N
            u = A[i][1]
            v = A[j][1]
            w = abs(A[i][0]-A[j][0])
            edges.append((w, u, v))
    edges.sort()

    parent = [i for i in range(N)]

    answer = 0
    # Kruskal's MST (union-find)
    for w, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            answer += w

    sys.stdout.write(f'{answer}\n')


if __name__ == '__main__':
    # sys.setrecursionlimit(int(1e6))
    # T = int(sys.stdin.readline())
    # for tid in range(1, T+1):
    #     testcase(tid)
    testcase(0)
