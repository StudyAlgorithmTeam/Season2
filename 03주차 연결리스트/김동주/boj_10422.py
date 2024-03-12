from functools import cache
from sys import stdin
from sys import stdout
from typing import List


MOD = int(1e9+7)

L = '('
R = ')'


def mmul(a: int, b: int, mod: int = MOD) -> int:
    return ((a % mod) * (b % mod)) % mod


@cache
def backtrack(L: int) -> int:
    if L == 1:
        return 0
    if L == 2:
        return 1
    # (S), ()S
    return mmul(2, backtrack(L-2))


for t in range(int(stdin.readline())):
    stdout.write(backtrack(int(stdin.readline())).__str__()+'\n')
