from functools import reduce
from itertools import permutations
from sys import stdin
from sys import stdout
from sys import maxsize


W_UNREACHABLE = 0

N = int(stdin.readline())
W = [ list(map(int, stdin.readline().split())) for _ in range(N) ]


def tsp(perm):
    w = 0
    for i in range(N):
        u, v = perm[i], perm[(i+1) % N]
        if W[u][v] == W_UNREACHABLE:
            return maxsize
        w += W[u][v]
    return w


def tsp_all():
    return min(tsp(perm) for perm in permutations(range(N)))

stdout.write(str(tsp_all()))
stdout.write('\n')
