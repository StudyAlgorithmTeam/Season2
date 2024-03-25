from sys import stdin
from sys import stdout
from sys import maxsize


N, M = map(int, stdin.readline().split())
apps = list(zip(
    map(int, stdin.readline().split()),
    map(int, stdin.readline().split()),
))


def dp(index=0, memory=0) -> int:
    if memory >= M:
        return 0
    if index >= N:
        return maxsize
    return min(
        dp(index+1, memory+apps[index][0]) + apps[index][1],
        dp(index+1, memory),
    )


stdout.write(dp().__str__()+'\n')
