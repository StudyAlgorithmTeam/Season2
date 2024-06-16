# 행성 탐사

import sys


J = 0
O = 1
I = 2

STR2INT = {'J': J, 'O': O, 'I': I}


if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())
    CNT = [[[0]*3 for x in range(N+1)] for y in range(M+1)]
    for y in range(1, M+1):
        for x, val in enumerate(sys.stdin.readline().strip(), start=1):
            CNT[y][x][J] = CNT[y][x-1][J] + CNT[y-1][x][J] - CNT[y-1][x-1][J]
            CNT[y][x][O] = CNT[y][x-1][O] + CNT[y-1][x][O] - CNT[y-1][x-1][O]
            CNT[y][x][I] = CNT[y][x-1][I] + CNT[y-1][x][I] - CNT[y-1][x-1][I]
            CNT[y][x][STR2INT[val]] += 1
    for i in range(K):
        y0, x0, y1, x1 = map(int, sys.stdin.readline().split())
        j = CNT[y1][x1][J] - CNT[y1][x0-1][J] - CNT[y0-1][x1][J] + CNT[y0-1][x0-1][J]
        o = CNT[y1][x1][O] - CNT[y1][x0-1][O] - CNT[y0-1][x1][O] + CNT[y0-1][x0-1][O]
        i = CNT[y1][x1][I] - CNT[y1][x0-1][I] - CNT[y0-1][x1][I] + CNT[y0-1][x0-1][I]
        sys.stdout.write(f"{j} {o} {i}\n")
