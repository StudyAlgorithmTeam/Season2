# Power Levels (Large)

import sys
from math import ceil, log10


def solve(D: int) -> str:
    N = 9000
    for E in range(1, N+1):
        # 근사 없이도 해보고, round도 해보고 ceil 도 해봤는데, 왜 ceil만 정답인지 모르겠다.
        if D > ceil(sum(map(log10, range(N,1,-E)))):
            return "IT'S OVER 9000" + "!"*E
    return "..."


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for t in range(1, T+1):
        D = int(sys.stdin.readline())
        sys.stdout.write(f"Case #{t}: {solve(D)}\n")
