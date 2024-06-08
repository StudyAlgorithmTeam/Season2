# 초콜릿 뺏어 먹기

import sys


N, K = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))


chocolates_per_day = []
for i in reversed(range(N)):
    if a[0] < a[i]:
        chocolates_per_day.append(a[i] - a[0])

print(sum(chocolates_per_day), len(chocolates_per_day))
