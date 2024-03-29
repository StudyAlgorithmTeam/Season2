from functools import cache
from sys import stdin
from sys import stdout
from sys import maxsize
from typing import Iterable


def bset_add(s: int, x: int) -> int:
    s |= 1 << x
    return s

def bset_remove(s: int, x: int) -> int:
    s &= ~(1 << x)
    return s

def bset_len(s: int) -> int:
    l = 0
    while s:
        if s & 1:
            l += 1
        s >>= 1
    return l

def bset_iter(s: int) -> Iterable[int]:
    i = 0
    while s:
        if s & 1:
            yield i
        i += 1
        s >>= 1


W_UNREACHABLE = 0

N = int(stdin.readline())
W = [list(map(int, stdin.readline().split())) for _ in range(N)]


@cache
def C(S: int, i: int = 0) -> int:
    # the cost of the minimum cost path visiting each vertex in set S exactly once,
    if bset_len(S) == 1:
        return W[0][i] if W[0][i] != W_UNREACHABLE else maxsize

    w = maxsize
    for j in bset_iter(S):
        if W[j][i] != W_UNREACHABLE:
            w = min(C(bset_remove(S, i), j)+W[j][i], w)
    return w


ans = C((1 << N)-1)
stdout.write(str(ans))
stdout.write('\n')
