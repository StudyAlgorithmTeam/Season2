# 화분 부수기

import sys


N = int(sys.stdin.readline())

count = 0
visited = [False] * int(1e6+1)

for i in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    if not (visited[a] or visited[b] or visited[c]):
        count += 1
    visited[a] = visited[b] = visited[c] = True

print(count)
