# 스펀지

import sys


MOD = 998244353

W, H, K, T = map(int, sys.stdin.readline().split())


def mult(*args: int) -> int:
    res = 1
    for n in args:
        res *= n % MOD
        res %= MOD
    return res


def area(x: int, y: int) -> int:
    y_max = min(y+T, H)
    y_min = max(y-T, 1)
    x_max = min(x+T, W)
    x_min = max(x-T, 1)
    return mult(x_max-x_min+1, y_max-y_min+1)


ans = 1
for i in range(1, K+1):
    x, y = map(int, sys.stdin.readline().split())
    ans = mult(ans, area(x, y))
print(ans)
