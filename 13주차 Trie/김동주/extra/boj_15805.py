# 트리 나라 관광 가이드

import sys


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
K = max(A)+1

parent_of = [-1] * K
parent = -1

for i in range(N):
    if parent_of[parent] != A[i]:
        parent_of[A[i]] = parent
    parent = A[i]


print(K)
print(*parent_of)
