# 양팔저울

from collections import deque
from typing import *
import sys


def solve():
    N = int(sys.stdin.readline())
    G = list(map(int, sys.stdin.readline().split()))
    S = sum(G)

    G.sort()
    G.reverse()

    possible = [False] * (2*S+2)

    q = deque([0])
    possible[0] = True

    for i in range(N):
        for j in range(len(q)):
            s = q.popleft()
            for g in (s+G[i], s, s-G[i]):
                possible[g] = True
                q.append(g)
    while q:
        g = q.popleft()
        possible[g] = True

    count = 0
    for n in range(1, S+1):
        if not possible[n]:
            count += 1

    print(count)



if __name__ == "__main__":
    solve()
