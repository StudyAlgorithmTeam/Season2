# 규칙적인 보스돌이

from typing import *
import sys
import math


MAX_SECONDS = 15 * 60


def solve() -> int:
    P_sorted = [0] * K
    Q_sorted = [0] * K
    for si, i in enumerate(sorted(range(K), key=lambda i: -Q[i]/P[i])):
        P_sorted[si] = P[i]
        Q_sorted[si] = Q[i]
    simulated = [
        simulate_character(P_sorted, Q_sorted, d_i, K-1, MAX_SECONDS) for d_i in range(N)
    ]
    return sum(sorted(simulated)[-M:])


def simulate_character(P: List[int], Q: List[int], d_i: int, k_i: int, t: int) -> int:
    # 0/1 Knapsack-like
    if k_i < 0:
        return 0
    dt = math.ceil(P[k_i]/D[d_i])
    return max(
        simulate_character(P, Q, d_i, k_i-1, t),
        simulate_character(P, Q, d_i, k_i-1, t-dt)+Q[k_i] if dt <= t else 0,
    )


if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().split())
    D = [0] * N
    P = [0] * K
    Q = [0] * K
    for i in range(N):
        D[i] = int(sys.stdin.readline())
    for i in range(K):
        P[i], Q[i] = map(int, sys.stdin.readline().split())
    ans = solve()
    print(ans)
