# 복권 + 은행

import functools
import sys

sys.setrecursionlimit(int(1e6))


N = int(sys.stdin.readline())
BALANCE = list(map(int, sys.stdin.readline().split()))
J = int(sys.stdin.readline())
C = int(sys.stdin.readline())

TOTAL_BALANCE = sum(BALANCE)


@functools.cache
def expect(balance: int, c: int = 0) -> int:
    if c == C:
        return balance
    p = balance / (TOTAL_BALANCE + J*c)
    return p * expect(balance+J, c+1)  + (1-p) * expect(balance, c+1)


print(expect(BALANCE[0]))
