import functools
import sys


N = int(sys.stdin.readline())
shape = [tuple(map(int, sys.stdin.readline().split())) for i in range(N)]


@functools.cache
def dp(i: int, j: int) -> int:
    if i+1 == j:
        return shape[i][0] * shape[i][1] * shape[j][1]
    return min([dp(i, k) + dp(k+1, j) for k in range(i+1, j)], default=sys.maxsize)


sys.setrecursionlimit(N*4)
sys.stdout.write(f'{dp(0, N-1)}\n')
