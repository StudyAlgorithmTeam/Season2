# 스케이트보드

import sys


max_score = 0

N = int(sys.stdin.readline())
for i in range(N):
    run_1, run_2, *tricks = map(int, sys.stdin.readline().split())
    score = max(run_1, run_2) + sum(sorted(tricks)[-2:])
    if max_score < score:
        max_score = score

print(max_score)
