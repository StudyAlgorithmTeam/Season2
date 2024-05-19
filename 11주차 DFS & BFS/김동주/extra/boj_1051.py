# 숫자 정사각형

from typing import *
import sys

N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().strip())) for i in range(N)]

ans = 0
for l in range(min(N, M)):
    for y in range(N-l):
        for x in range(M-l):
            if len(set([grid[y][x], grid[y+l][x], grid[y][x+l], grid[y+l][x+l]])) == 1:
                ans = (l+1)**2

print(ans)
