import functools
import sys
import typing


MAX_N = 500

N = int(sys.stdin.readline())

shape = []
for i in range(N):
    r, c = map(int, sys.stdin.readline().split())
    shape.append((r, c))


@functools.cache
def dp(i: int, r: int) -> typing.Tuple[int, int]: # value, c
    if i == N-1:
        return 0, shape[i][1]

    ans = []

    # 나를 먼저 곱할 때 = (AB)C
    ops = r * shape[i][1] * shape[i+1][1]
    val, c = dp(i+1, r)
    ans.append((ops+val, min(c, shape[i+1][1])))

    # 나를 나중에 곱할 때 = A(BC)
    val, c = dp(i+1, shape[i+1][0])
    ops = r * shape[i][1] * c
    ans.append((ops+val, c))

    return min(ans)


sys.setrecursionlimit(MAX_N*4)
sys.stdout.write(f'{dp(0, shape[0][0])[0]}\n')
