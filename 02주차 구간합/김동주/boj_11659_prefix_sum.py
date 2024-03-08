import sys
from typing import *


N, M = map(int, sys.stdin.readline().split())

# 사전에 계산해두는 acc[i] = 1번째 원소부터 i번째 원소까지의 합. (accumulate)
acc: List[int] = [0]
for value in map(int, sys.stdin.readline().split()):
    acc.append(acc[-1] + value)

# 구간 질의 시작
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(acc[j]-acc[i-1])+'\n')
